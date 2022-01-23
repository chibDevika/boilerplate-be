from leavestracker.apps.employees.models import CustomUser
from leavestracker.apps.employees.serializers import EmployeesSerializer
from leavestracker.apps.employees import constants

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

class EmployeesView(APIView):
    serializer_class = EmployeesSerializer
    authentication_classes = []
    permission_classes = [AllowAny,]
    
    def get_queryset(self):
        user=CustomUser.objects.filter(username=self.request.data['username']).first()
        return user

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                user = self.get_queryset()
                token, created  = Token.objects.create(user=user)
                response = {"data": serializer.data, "token": token.key}
                (data, response_status) = (response, status.HTTP_201_CREATED)
        except Exception as ex:
            if str(ex) == constants.SAME_USER_ERROR:
                user = self.get_queryset()
                token, created = Token.objects.get_or_create(user=user)
                response = {"data": EmployeesSerializer(instance=user).data, "token": token.key}
                (data, response_status) = (response, status.HTTP_200_OK)
            else:
                data = [constants.WORK_IN_PROGRESS]
                (data, response_status) = (data, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data, response_status)

