from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken
# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with router(ViewSet)
# router.register('studentapi',views.StudentViewSet,basename='student')

# Register StudentViewSet with router(ModelViewSet)
router.register('studentapi',views.StudentModelViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),#BasicAuthentication
    path('session', include('rest_framework.urls',namespace='rest_framework')),#SessionAuthentication
    #path('gettoken/',obtain_auth_token),#TokenAuthentication also for sending request need to install httpie
    path('gettoken/',CustomAuthToken.as_view()),#for custom token mnj token generate jhala ki responce mdhi ky pahij ajun te

]
