from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "Access Denied: Owner user only"

    def has_object_permission(self, request, view, obj):
        return bool(obj.owner == request.user.id)


class IsAdmin(permissions.BasePermission):
    message = "Access Denied: Admin Only"

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and "ADMIN" in request.user.role
        )
