from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UsersSerializer, ContentSerializer, Categories
from .constants import *
from .data_validations import validate_request

from .models import *

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'create':'api/create',
        'update':'api/update'
    }
    #return JsonResponse("API Response", safe= False)
    return Response(api_urls)

@api_view(['POST'])
def userSave(request):
    serializer = UsersSerializer(data=request.data)
    data,status = validate_request(request)
    if not status:
        return Response(data)
    if serializer.is_valid():
        serializer.save()
    return Response({'status':SUCCESS,'data':serializer.data})

@api_view(['POST'])
def contentSave(request):
    user = Users.objects.get(id=request.data['user_id'])
    if user.type_of_user == USER_ADMIN:
        return Response({'status':FAILURE,'data':ADMIN_USER_CANNOT_ADD_CONTENT})     
    new_content = Content.objects.create(user= user, title=request.data['title'],body= request.data['body'],
                                         summary= request.data['summary'] )
    new_content.save()
    serializer = ContentSerializer(new_content)
    print(request.data['categories'])
    for category in request.data['categories']:
        Categories.objects.create(content = new_content, category_name= category).save()
    return Response({'status':SUCCESS,'data':serializer.data})

@api_view(['GET'])
def contentView(request, user_id):
    user = Users.objects.get(id=int(user_id))
    print(user.type_of_user)
    if user.type_of_user == USER_ADMIN:
        content = Content.objects.all()
    else:
        content = Content.objects.filter(user=int(user_id))
    serializer = ContentSerializer(content, many = True)
    return Response({'status':SUCCESS,'data':serializer.data})

@api_view(['POST'])
def contentUpdate(request):
    content = Content.objects.get(id=int(request.data['content_id']))
    user = Users.objects.get(id=int(request.data['user_id']))
    if content.user.id != request.data['user_id'] and user.type_of_user != USER_ADMIN:
        return Response({'status':FAILURE,'data':NO_ACCESS_TO_EDIT_CONTENT}) 
    content.title = request.data['title']
    content.body = request.data['body']
    content.summary = request.data['summary']
    content.save()
    for category in request.data['categories']:
        Categories.objects.create(content = content, category_name= category).save()
    serializer = ContentSerializer(content)
    return Response({'status':SUCCESS,'data':serializer.data})
    