from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('signup', views.SignupView.as_view()),
    path('login', views.AuthTokenView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('verify', TokenVerifyView.as_view()),
    path('info', views.UserProfile.as_view()),
]