from django.urls import path

from donations.apps import DonationsConfig
from donations.views import DonationsCreateAPIView

app_name = DonationsConfig.name

urlpatterns = [
    path("course/<int:pk>/donate/", DonationsCreateAPIView.as_view(), name="donate")
]
