from leavestracker.apps.employees.models import CustomUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from leavestracker.apps.employees.serializers import EmployeesSerializer
from leavestracker.apps.employees import constants

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
        except Exception as ex:
            if str(ex) == constants.same_user_error_message:
                user = self.get_queryset()
                (data, response_status) = (EmployeesSerializer(instance=user).data, status.HTTP_200_OK)
            else:
                data = [constants.work_in_progress]
                (data, response_status) = (data, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data, response_status)

