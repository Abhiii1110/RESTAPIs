from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Student
from . serializers import StudentSerializer
from rest_framework.views import APIView


# Create your views here.
# FUNCTION BASED API VIEW
# @api_view(['GET','POST','PUT','DELETE'])
# def student_api(request):
#     if request.method == 'GET':
#         id = request.data.get('id')
#         if id is not None:
#             #for single data/object by id
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)

#          #For All DATA/Objects
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)

#     #POST MEthod
#     if request.method == "POST":
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"Data Created"})
#         return Response(serializer.errors)

#     #PUT Method
#     if request.method == "PUT":
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"Data Updated"})
#         return Response(serializer.errors)

#     #DELETE Method
#     if request.method == "DELETE":
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({"Msg":"Data DELETED"})

#------------------------------------------------------------------------------------------------------#
# CLASS BASED API VIEW
class StudentAPI(APIView):
    def get(self,request,format=None,pk=None):
        id = pk
        if id is not None:
            #for single data/object by id
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        #For All DATA/Objects
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Created"})
        return Response(serializer.errors)

    def put(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Full/Complete Data Updated"})
        return Response(serializer.errors)

    def patch(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Updated"})
        return Response(serializer.errors)

    def delete(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"Msg":"Data DELETED"})
