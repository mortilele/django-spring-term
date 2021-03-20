from rest_framework import viewsets
from main.models import Book, Journal
from main.serializers import BookModelSerializer, JournalModelSerializer
from users.permissions import AdminRolePermission

MODIFY_REQUEST_METHODS = ['create', 'update', 'partial_update', 'delete']


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()

    def get_permissions(self):
        if self.action in MODIFY_REQUEST_METHODS:
            self.permission_classes = [AdminRolePermission]
        return super().get_permissions()


class JournalViewSet(viewsets.ModelViewSet):
    serializer_class = JournalModelSerializer
    queryset = Journal.objects.all()

    def get_permissions(self):
        if self.action in MODIFY_REQUEST_METHODS:
            self.permission_classes = [AdminRolePermission]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)