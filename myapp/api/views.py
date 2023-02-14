from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

def hello(request):
    return HttpResponse('hello')

class ClientSignupView(generics.GenericAPIView):
    serializer_class = ClientSignupSerializer
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })


class ManagertSignupView(generics.GenericAPIView):
    serializer_class = ManagerSignupSerializer
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })


class EmploeeSignupView(generics.GenericAPIView):
    serializer_class = EmployeeSignupSerializer
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })

@csrf_exempt
def task_api(request,id=0):
    if request.method == 'GET':
        task = Task.objects.all()
        task_serializer = TaskSerializer(task,many=True)
        return JsonResponse(task_serializer.data,safe=False)
    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Task added successfully",safe=False)
    elif request.method == 'PUT':
        task_data = JSONParser().parse(request)
        task = Task.objects.get(id=task_data['TaskId'])
        task_serializer = TaskSerializer(task,data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Task updated successfully",safe=False)
        return JsonResponse("Failed to update")
    elif request.method == 'DELETE':
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse("Task deleted successfullu",safe=False)
