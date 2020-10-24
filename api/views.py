from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UsersSerializer
from .constants import *
from .data_validations import validate_request

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
    