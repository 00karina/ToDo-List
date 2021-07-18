from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls={
        'List':'/list/',
        'Detail View':'/detail/<str:pk>/',
        'Create':'/create/',
        'Update':'/update/<str:pk>/',
        'Delete':'/delete/<str:pk>/',
    

    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks=Task.objects.all()
    print(tasks)
    serializer=TaskSerializer(tasks,many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    tasks=Task.objects.get(id=pk)
    print(tasks)
    serializer=TaskSerializer(tasks)
    print(serializer)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def taskUpdate(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def taskDelete(request,pk):
    tasks=Task.objects.get(id=pk)
    tasks.delete()
    
    return Response('Item successfully delete')

