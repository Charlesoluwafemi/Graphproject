# api/serializers.py

from rest_framework import serializers
from .models import Namespace, DataUpload

class NamespaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Namespace
        fields = '__all__'

class DataUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUpload
        fields = '__all__'
