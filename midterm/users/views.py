from rest_framework import generics
from rest_framework.response import Response

from users.serializers import RegisterSerializer, UserModelSerializer


class UserRegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserModelSerializer(user, context=self.get_serializer_context()).data)
