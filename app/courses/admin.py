from django.contrib import admin


from .models import Courses, UsersCourses, Users

admin.site.register(Courses)
admin.site.register(UsersCourses)
admin.site.register(Users)
# Register your models here.
