from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from leavestracker.apps.employees.models import Employees
from leavestracker.apps.employees.serializers import EmployeesSerializer

class EmployeesView(APIView):
    def post(self, request):
        user = Employees.object.get(username = request.username)
        if user:
            return Response(status=status.HTTP_200_OK)
        else:
            serializer = EmployeesSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
