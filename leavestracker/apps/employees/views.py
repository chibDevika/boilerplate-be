from django.http import request
from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import EmployeesSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
    def create(self, request):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

