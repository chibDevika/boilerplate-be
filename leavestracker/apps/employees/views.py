from leavestracker.apps.employees.models import CustomUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from leavestracker.apps.employees.serializers import EmployeesSerializer

class EmployeesView(APIView):
    serializer_class = EmployeesSerializer
    
    def get_queryset(self):
        user=CustomUser.objects.filter(username=self.request.data['username']).first()
        return user

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                (data, response_status) = (serializer.data, status.HTTP_201_CREATED)
        except Exception:
            user = self.get_queryset()
            (data, response_status) = (EmployeesSerializer(instance=user).data, status.HTTP_200_OK)
        return Response(data ,response_status)

