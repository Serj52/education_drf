from .models import Users, Courses
from rest_framework import serializers


class UsersSerialize(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class CoursesSerialize(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"