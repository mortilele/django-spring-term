from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import ToDoGroup, ToDoItem
from main.serializers import ToDoGroupSerializer, ToDoSerializer


class ToDoGroupViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = ToDoGroup.objects.all().prefetch_related('todos')
    serializer_class = ToDoGroupSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'completed':
            return ToDoSerializer
        return self.serializer_class

    @action(methods=['get'], detail=True)
    def completed(self, request, *args, **kwargs):
        group = self.get_object()
        serializer = self.get_serializer(group.todos.filter(status=ToDoItem.DONE), many=True)
        return Response(serializer.data)
