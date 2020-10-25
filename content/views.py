from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ContentSerializer, Categories
from api.constants import *
from .models import *
from user.models import Users

@api_view(['POST'])
def contentSave(request):
    user = Users.objects.get(id=request.data['user_id']) #Getting User Object
    if user.type_of_user == USER_ADMIN:
        # Condition for not allowing admin user to add any content
        return Response({'status':FAILURE,'data':ADMIN_USER_CANNOT_ADD_CONTENT})     
    new_content = Content.objects.create(user= user, title=request.data['title'],body= request.data['body'],
                                         summary= request.data['summary'] )
    new_content.save() #Saving the content
    serializer = ContentSerializer(new_content)
    print(request.data['categories'])
    for category in request.data['categories']:
        #Added categories in database
        Categories.objects.create(content = new_content, category_name= category).save()
    return Response({'status':SUCCESS,'data':serializer.data})

@api_view(['GET'])
def contentView(request, user_id):
    try:
        user = Users.objects.get(id=int(user_id))
        if user.type_of_user == USER_ADMIN:
            # Check if user is admin then return all the contents
            content = Content.objects.all()
        else:
            # Return contents of specific user
            content = Content.objects.filter(user=int(user_id))
        serializer = ContentSerializer(content, many = True)
        return Response({'status':SUCCESS,'data':serializer.data})
    except ObjectDoesNotExist:
        return Response({'status':FAILURE,'data':NO_CONTENT_AVAILABLE}) 
    
@api_view(['POST'])
def contentUpdate(request):
    try:
        content = Content.objects.get(id=int(request.data['content_id']))
        user = Users.objects.get(id=int(request.data['user_id']))
        if content.user.id != request.data['user_id'] and user.type_of_user != USER_ADMIN:
            # Check for not allowing other user to edit the content
            return Response({'status':FAILURE,'data':NO_ACCESS_TO_EDIT_CONTENT}) 
        content.title = request.data['title']
        content.body = request.data['body']
        content.summary = request.data['summary']
        content.save()
        for category in request.data['categories']:
            Categories.objects.create(content = content, category_name= category).save()
        serializer = ContentSerializer(content)
        return Response({'status':SUCCESS,'data':serializer.data})
    except ObjectDoesNotExist:
        return Response({'status':FAILURE,'data':NO_CONTENT_AVAILABLE}) 
    
@api_view(['DELETE'])
def contentDelete(request):
    try:
        content = Content.objects.get(id=int(request.data['content_id']))
        print(content)
        user = Users.objects.get(id=int(request.data['user_id']))
        if content.user.id != request.data['user_id'] and user.type_of_user != USER_ADMIN:
            # Check for not allowing other user to delete the content
            return Response({'status':FAILURE,'data':NO_ACCESS_TO_DELETE_CONTENT}) 
        count = Content.objects.get(id=int(request.data['content_id'])).delete()
        return Response({'status':SUCCESS,'data':SUCCESSFULLY_DELETED_RECORDS.format(str(count))})
    except ObjectDoesNotExist:
        return Response({'status':FAILURE,'data':NO_CONTENT_AVAILABLE})
    
@api_view(['GET'])
def contentSearch(request, search_text):
    try:
        from django.db.models import Q
        categories = Categories.objects.filter(category_name__contains = search_text)
        content_ids = []
        #Fetched all the categories with the text and content id corresponding to it
        for category in categories:
            content_ids.append(category.content_id)
        #Fetched all the contents with contains clause which considers substring as well
        content = Content.objects.filter(Q(title__contains = search_text) | Q(body__contains = search_text) | Q(summary__contains = search_text)
                                         | Q(id__in = content_ids))
        serializer = ContentSerializer(content, many = True)
        return Response({'status':SUCCESS,'data':serializer.data})
    except ObjectDoesNotExist:
        return Response({'status':FAILURE,'data':NO_CONTENT_AVAILABLE})
        
    