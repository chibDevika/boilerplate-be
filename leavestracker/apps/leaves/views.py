from logging import raiseExceptions
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from leavestracker.apps.leaves.serializer import LeaveSerializer
from leavestracker.apps.leaves.models import Leaves
from rest_framework import serializers

class LeavesView(APIView):

    def post(self,request):
        serializer = LeaveSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def get(self, request, id=None):
        if id:
            try:
                leaves=Leaves.objects.get(id=id)
                serializer=LeaveSerializer(leaves)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
            except Leaves.DoesNotExist:
                try: 
                    leaves=Leaves.objects.get(employee_id=id)
                    serializer=LeaveSerializer(leaves, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)

                except:
                    return Response("Leave hasn't been applied for the selected dates or user.", status=status.HTTP_200_OK)

        leaves=Leaves.objects.all()
        serializer=LeaveSerializer(leaves, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        try:
            leaves=Leaves.objects.get(id=id)
            serializer=LeaveSerializer(leaves ,data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Leaves.DoesNotExist:
            return Response("The leave you're trying to update, doesn't exist.", status=status.HTTP_200_OK)
