from rest_framework import permissions

# permission created so that the logged in user can only access its own notes
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user