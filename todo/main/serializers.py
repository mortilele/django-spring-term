from rest_framework import serializers
from main.models import ToDoGroup, ToDoItem
from users.serializers import UserSerializer


class ToDoGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoGroup
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = ToDoItem
        fields = '__all__'
