from django.contrib import admin
from .models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','roll','city')
    search_fields= ('name','city')
    list_filter = ('city',)


admin.site.register(Student,StudentAdmin)