from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from leavestracker.apps.employees.serializers import EmployeesSerializer

class EmployeesView(APIView):
    def post(self, request):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
