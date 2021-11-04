from rest_framework import serializers
from .models import HelloWorld

class HelloSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=255)

    def list(self):
        return HelloWorld.object.all()