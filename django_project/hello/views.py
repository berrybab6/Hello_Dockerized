from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from hello.serializers import HelloSerializer
from rest_framework import viewsets
from rest_framework import generics, permissions,status
from rest_framework.permissions import IsAdminUser
from .models import Hello
# Create your views here.
class HelloView(generics.GenericAPIView):

    queryset = Hello.objects.all()
    serializer_class = HelloSerializer
    permission_classes = (permissions.AllowAny, )
    def get(self, request,format=None):
        user = Hello.objects.all()
        serialize = HelloSerializer(user,many=True)
        return JsonResponse(serialize.data,safe=False, status=status.HTTP_200_OK)