from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UsersSerializer
from api.constants import *
from .data_validation import validate_request

from .models import *

@api_view(['POST'])
def userSave(request):
    serializer = UsersSerializer(data=request.data)
    data,status = validate_request(request)
    if not status:
        return Response(data)
    if serializer.is_valid():
        serializer.save()
    return Response({'status':SUCCESS,'data':serializer.data})