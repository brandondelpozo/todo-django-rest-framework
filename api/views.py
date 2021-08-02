from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

#from django.views.decorators.csrf import ensure_csrf_cookie
#from django.views.decorators.csrf import csrf_exempt

from .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delate/<str:pk>/',
    }

    return Response(api_urls)

#@csrf_exempt
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

#@csrf_exempt
@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

#@ensure_csrf_cookie
@api_view(['POST'])
#@csrf_exempt
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#@csrf_exempt
@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#@csrf_exempt
@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item succesfully deleted!')