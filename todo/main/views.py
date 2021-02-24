from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from main.models import ToDoGroup, ToDoItem


class ToDoGroupViewSet(mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = ToDoGroup.objects.all().prefetch_related('todos')
    renderer_classes = [TemplateHTMLRenderer]

    def retrieve(self, request, *args, **kwargs):
        group = self.get_object()
        return Response({
            'group_name': group.name,
            'todos': group.todos.filter(status=ToDoItem.IN_PROGRESS)
        },
            template_name='todo_list.html')

    @action(methods=['get'], detail=True)
    def completed(self, request, *args, **kwargs):
        group = self.get_object()
        return Response({
            'group_name': group.name,
            'todos': group.todos.filter(status=ToDoItem.DONE)
        },
            template_name='completed_todo_list.html')
