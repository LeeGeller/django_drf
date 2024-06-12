from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import PaymentsListAPIView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    # Payments
    path("payments/", PaymentsListAPIView.as_view(), name="payments-list"),
    # User
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
