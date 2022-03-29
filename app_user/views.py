from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from .models import UserMbtiHistory
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from .serializers import SignupSerializer, CustomTokenPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView


class SignupView(CreateAPIView):
    model = User
    authentication_classes = (TokenAuthentication, )
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]


class AuthTokenView(TokenObtainPairView):
    serializer_class = CustomTokenPairSerializer


class UserProfile(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        uid = request.user.pk
        usr = User.objects.get(id=uid)
        mbti_history = UserMbtiHistory.objects.filter(uid=usr).order_by('-created_at')
        mbti = mbti_history[0].mbti if len(mbti_history) > 0 else None
        return Response(data={"mbti": mbti}, status=status.HTTP_200_OK)