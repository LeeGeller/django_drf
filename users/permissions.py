from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = "You must be moderator"

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()


class IsOwner(BasePermission):
    message = "You must be owner"

    def has_permission(self, request, view):
        return request.user.owner == request.user
