from django.contrib import admin
from main.models import ToDoGroup, ToDoItem


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'due_date', 'status', 'owner', 'group')
    list_filter = ('status', 'group', 'owner')
    list_editable = ('status', )
    search_fields = ('owner__username', 'group__name')


class ToDoItemInline(admin.TabularInline):
    model = ToDoItem
    extra = 1


@admin.register(ToDoGroup)
class ToDoGroupModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )
    inlines = [ToDoItemInline]
