from django.contrib import admin
from . models import TodoItem
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TodoItem._meta.get_fields()]


admin.site.register(TodoItem,TodoAdmin)