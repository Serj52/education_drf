from .models import Users
from rest_framework import serializers


class UsersSerialize(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

