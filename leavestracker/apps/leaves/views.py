from datetime import datetime
from django.db.models import Q

from leavestracker.apps.leaves.serializer import LeaveSerializer
from leavestracker.apps.leaves.models import Leaves
from leavestracker.apps.leaves import constants

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class LeavesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
 

    def get(self, request, start=None, end=None, id=None):
        if id:
            try:
                leaves=Leaves.objects.get(id=id)
                serializer=LeaveSerializer(leaves)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
            except Leaves.DoesNotExist:
                return Response(constants.LEAVE_DOES_NOT_EXIST, status=status.HTTP_400_BAD_REQUEST)
        startDate = datetime.strptime(start, '%Y-%m-%d')
        endDate = datetime.strptime(end, '%Y-%m-%d')
        leaves=Leaves.objects.filter((Q(started_at__gte=startDate) & Q(started_at__lte=endDate)) | (Q(ended_at__gte=startDate) & Q(ended_at__lte=endDate)))
        serializer=LeaveSerializer(leaves, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, id=None):
        try:
            leaves=Leaves.objects.get(id=id)
            print(leaves.id, request.data)
            serializer=LeaveSerializer(leaves, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Leaves.DoesNotExist:
            return Response(constants.LEAVE_DOES_NOT_EXIST, status=status.HTTP_400_BAD_REQUEST)
