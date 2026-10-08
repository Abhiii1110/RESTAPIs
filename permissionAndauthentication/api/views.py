# from .models import Student
# from rest_framework import viewsets
# from .serializers import StudentSerializer
# from rest_framework.response import Response


# class StudentViewSet(viewsets.ViewSet):

#     def list(self, request):
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         stu = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(stu)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "Data Created"})
#         return Response(serializer.errors)

#     def update(self, request, pk=None):
#         stu = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "Data Updated"})
#         return Response(serializer.errors)

#     def partial_update(self, request, pk=None):
#         stu = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "Data Partially Updated"})
#         return Response(serializer.errors)

#     def destroy(self, request, pk=None):
#         stu = Student.objects.get(pk=pk)
#         stu.delete()
#         return Response({"msg": "Data Deleted"})

# ------------------------------------------------------------------------------------------------------------------


from . models import Student
from . serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
#SessionAuthentication #BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from . custompermissions import MyPermission


# BasicAuthentication And Permissions
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     # je jyast Class aste aplyakd tr sglyanmdhi he authentication ani permission liht bsyla lgl ast techya pekshya setting.py mdhi globally mention krych srk srk ith(views.py) mdhi mention kryla nai lgt
    
#     authentication_classes = [BasicAuthentication]
#     # permission_classes = [ IsAuthenticated]
#     # permission_classes = [ AllowAny]
#     permission_classes = [ IsAdminUser]#jya user ch IsStaff true asl toch fkt login kru shakto
    
#SESSION AUTHENTICATION
# Session authentication sathi urls.py mdhi mention kryla lgt teva tith login ch option yet
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     authentication_classes = [SessionAuthentication]
    # permission_classes = [ IsAuthenticated]
    
    # permission_classes = [ AllowAny]
    
    # permission_classes = [ IsAdminUser]#jya user ch IsStaff true asl toch fkt login kru shakto
    
    # permission_classes = [ IsAuthenticatedOrReadOnly]#Authenticated user login krun get read write delete sgl kru shakto pn jo authenticated nhiye to fkt read mnj get kru shakto fkt bghu shakto bss
    
    # permission_classes = [ DjangoModelPermissions]#same ahe fkt backend mdhun apan je je permission deil te sgl kru shakto to and by default techyakd fkt login krun get ani read kru shakto
    
    #permission_classes = [ DjangoModelPermissionsOrAnonReadOnly]#hechyat login nai kel tri data bghu shakto fkt jri login kel ani backend mdhi user la sermission nasl tr to fkt get kru shakto ani read bghu shakto jr backend mdhi je je permission ahe tech fkt kru shakto ani isStaff true asl tri permission nasl backend mdhi tri ky kru nai shakat


#CUSTOM PERMISSIONS
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     authentication_classes = [SessionAuthentication]
#     permission_classes = [MyPermission]


#TOKEN AUTHENTICATION

#need to write in settings.py file
# installed_apps = [
# 'rest_framework.authtoken',
# ]
# after mentioning run py manage.py migrate

# There are multiple ways of creating or generating a token
# 1. using admin application/django admin panel
# 2. using django manage.py command
    # (py manage.py drf_create_token <username>)
# 3. By exposing an API endpoint(how client can ask/create token)
# 3rd method is this
# also for sending request need to install httpie
# for custom token authentication need to create auth.py file and write custom token mnj token generate jhal ki return mdhi generated token mdhi response mdhi token,user_id,email etc bhetal
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [SessionAuthentication]
    # permission_classes = [MyPermission]
