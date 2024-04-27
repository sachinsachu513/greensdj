from rest_framework import serializers
from .models import userregister
class userregisterserializer(serializers.ModelSerializer):
    class Meta:
        model=userregister
        fields="__all__"