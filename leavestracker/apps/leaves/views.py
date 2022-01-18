from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from leavestracker.apps.leaves.serializer import LeaveSerializer
from leavestracker.apps.leaves.models import Leaves
from leavestracker.apps.leaves import constants

class LeavesView(APIView):

    def post(self,request):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
 

    def get(self, request, id=None):
        if id:
            try:
                leaves=Leaves.objects.get(id=id)
                serializer=LeaveSerializer(leaves)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
            except Leaves.DoesNotExist:
                return Response(constants.LEAVE_DOES_NOT_EXIST, status=status.HTTP_200_OK)

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
            return Response(constants.LEAVE_DOES_NOT_EXIST, status=status.HTTP_200_OK)
