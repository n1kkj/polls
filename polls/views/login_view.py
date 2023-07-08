from polls.serializers.login_serializer import LoginSerializer
from rest_framework.response import Response
from rest_framework import views, status


class LoginView(views.APIView):

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return Response(data=token, status=status.HTTP_200_OK)