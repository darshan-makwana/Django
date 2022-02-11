from rest_framework import serializers

from .models import *

class UserInfoSerializer(serializers.ModelSerializer):
    Username=

    class Meta:
        model = UserInfo
        fields = '__all__'