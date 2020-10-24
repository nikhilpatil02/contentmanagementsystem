from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'create':'api/create',
        'update':'api/update'
    }
    #return JsonResponse("API Response", safe= False)
    return Response(api_urls)