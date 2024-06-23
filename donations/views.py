from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from donations.models import Donate
from donations.serializer import DonateSerializer
from donations.services import create_product


class DonationsCreateAPIView(CreateAPIView):
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        validated_data = serializer.validated_data
        print(validated_data.get("id"))
        # course = validated_data["course"]
        # course_for_donate = create_product(
        #     serializer.data["course"], serializer.data["user"]
        # )
