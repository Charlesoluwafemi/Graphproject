from django.shortcuts import render

# Create your views here.
# api/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .blazegraph_utils import connect_to_blazegraph, create_namespace, add_data
from .models import Namespace, DataUpload
from .serializers import NamespaceSerializer, DataUploadSerializer

@api_view(['POST'])
def create_database(request):
    serializer = NamespaceSerializer(data=request.data)
    if serializer.is_valid():
        bg_client = connect_to_blazegraph()
        create_namespace(bg_client, serializer.validated_data['name'])
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def upload_ttl(request):
    serializer = DataUploadSerializer(data=request.data)
    if serializer.is_valid():
        bg_client = connect_to_blazegraph()
        add_data(bg_client, serializer.validated_data['namespace'].name, serializer.validated_data['file'])
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from .blazegraph_utils import connect_to_blazegraph, create_namespace, add_data

def save_settings(request):
    if request.method == 'POST':
        namespace_name = request.POST.get('namespace_name')
        if create_namespace(namespace_name):
            return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})

def upload_file(request):
    if request.method == 'POST':
        namespace = request.POST.get('namespace')
        ttl_data = request.FILES['ttl_file'].read()
        if add_data(namespace, ttl_data):
            return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})
