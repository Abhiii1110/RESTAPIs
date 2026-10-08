from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')
    search_fields = ('name', 'city')          # adds a search box
    list_filter = ('city',)                   # adds filter sidebar
    ordering = ('name',)                      # default ordering
admin.site.register(Student,StudentAdmin)