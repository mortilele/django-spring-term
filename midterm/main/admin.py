from django.contrib import admin

# Register your models here.
from main.models import Journal, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
