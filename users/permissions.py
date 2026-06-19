from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and (
                request.user.is_superuser or
                request.user.groups.filter(name="moderator").exists()
            )
        )


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated and
            hasattr(obj, "owner") and
            obj.owner == request.user
        )
