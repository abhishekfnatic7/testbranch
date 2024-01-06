# serializers.py
from rest_framework import serializers
from .models import Third

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Third
        fields = '__all__'
