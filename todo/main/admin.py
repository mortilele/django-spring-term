from django.contrib import admin
from main.models import ToDoGroup, ToDoItem


class ToDoItemInline(admin.TabularInline):
    model = ToDoItem


@admin.register(ToDoGroup)
class ToDoGroupModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [ToDoItemInline]
