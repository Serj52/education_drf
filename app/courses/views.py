from django.shortcuts import render
from .serializers import UsersSerialize, CoursesSerialize
# Create your views here.
from rest_framework import generics, viewsets
from .models import Users, Courses
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from  .permisisons import IsAdminReadOnly


class UsersViwsets(viewsets.ModelViewSet):
    #Все методы CRUD в одном классе
    queryset = Users.objects.all()
    serializer_class = UsersSerialize

class UsersAPI(generics.ListCreateAPIView):
    # Чтение и запись в БД, Обрабатывает только POST и GET запросы
    queryset = Users.objects.all()
    serializer_class = UsersSerialize

class UsersAPIUpdate(generics.UpdateAPIView):
    #Обновление данных в БД. Обрабатывает PUT и PATCH запросы
    queryset = Users.objects.all()
    serializer_class = UsersSerialize

class CourseAPIHandler(generics.RetrieveUpdateDestroyAPIView):
    # Обрабатывает PUT, PATCH, GET, DELETE запросы
    queryset = Courses.objects.all()
    serializer_class = CoursesSerialize

@permission_classes([IsAdminReadOnly])
class CoursesAPI(generics.ListCreateAPIView):
    # Чтение и запись в БД, Обрабатывает только POST и GET запросы
    queryset = Courses.objects.all()
    serializer_class = CoursesSerialize



