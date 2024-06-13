from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = "You must be moderator"

    def has_permission(self, request, view):
        return request.user.groups.filter(name="managers").exists()


class IsOwner(BasePermission):
    message = "You must be the owner of this content."

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
