from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignInSerializer, GuestSigninSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create your views here.

class SignIn(APIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        try:
            if serializer.is_valid():
                user = serializer.save()
                return Response({
                    "message": f"signin successfull for user: {user.username}"
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({
                "message": f"Failed: {error}"
            }, status=status.HTTP_400_BAD_REQUEST)

class GuestSignin(APIView):

    def post(self, request):
        serializer = GuestSigninSerializer(data=request.data)
        try:
            if serializer.is_valid():
                user = serializer.save()
                return Response({
                    "message": f"signin successfull for user: {user.username}"
                })
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({
                "message": f"Failed: {error}"
            }, status=status.HTTP_400_BAD_REQUEST)

class Login(TokenObtainPairView):
    serializer = LoginSerializer