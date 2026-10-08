from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('StudentAPICRUD/', views.student_api),
    # path('StudentAPICRUD/<int:pk>', views.student_api),
    path('StudentAPICRUD/', views.StudentAPI.as_view()),
    path('StudentAPICRUD/<int:pk>', views.StudentAPI.as_view()),
]
