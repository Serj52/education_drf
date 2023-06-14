from rest_framework import permissions

class IsAdminReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #Разрешение чтения для не авторизованных пользователей
        if request.method in permissions.SAFE_METHODS:
            return True
        #Разрешение чтения для авторизованных пользователей
        return bool(request.user and request.user.is_staff)
