from django.db import models


# Create your models here.
class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UsersCourses(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "Users",
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        "Courses",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user, self.course
