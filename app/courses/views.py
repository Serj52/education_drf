from django.shortcuts import render
from .serializers import UsersSerialize
# Create your views here.
from rest_framework import generics
from .models import Users


class UsersAPI(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerialize
