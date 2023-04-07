from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import RegistrationSerializer, UsersSerializer
from rest_framework import permissions
import requests
from .models import Account


# Create your views here.
class CreateUserAccount(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        reg_serializer = RegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                res = requests.post('http://127.0.0.1:8000/api-auth/token', data={
                    'username': new_user.email,
                    'password': request.data['password'],
                    'client_id': 'pBqjrWArbv9G4ZoqGyegS8AhGfxifF4cPv9UaaA6',
                    'client_secret': '5LsbLLBS7f0F6686Oob1S6fUf1uVI70BALxLLQR89rgln5Q8PBteMKhjz9xdU5lODKUVkybz14FV9aR3UJjRtT13wECW0pcUrMqvPN6EJ7EEKer3QquMEGa6Alh0galk',
                    'grant_type': 'password'
                })
                return Response(res.json(), status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllUsers(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()
    serializer_class = UsersSerializer


class CurrentUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UsersSerializer(self.request.user)
        return Response(serializer.data)
