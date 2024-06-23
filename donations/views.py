from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from donations.models import Donate
from donations.serializer import DonateSerializer


class DonationsCreateAPIView(CreateAPIView):
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer
    permission_classes = (IsAuthenticated,)
