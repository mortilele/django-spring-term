from rest_framework import serializers

from main.models import Book, Journal
from users.serializers import UserModelSerializer


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class JournalModelSerializer(serializers.ModelSerializer):
    publisher = UserModelSerializer(read_only=True)

    class Meta:
        model = Journal
        fields = '__all__'
