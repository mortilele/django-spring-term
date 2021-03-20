from rest_framework.permissions import IsAuthenticated

from users.models import User


class AdminRolePermission(IsAuthenticated):

    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) and request.user.role == User.SUPER_ADMIN)
