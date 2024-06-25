from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from donations.models import Donate
from donations.serializer import DonateSerializer
from donations.services import create_donation


class DonationsCreateAPIView(CreateAPIView):
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        donate = serializer.save(user=self.request.user)
        validated_data = serializer.validated_data
        course_id, price = validated_data.get("course"), validated_data.get("amount")

        course, session_id, donate_url = create_donation(
            course_id, self.request.user, price
        )

        donate.course = course_id
        donate.amount = price
        donate.donate_url = donate_url
        donate.session_id = session_id
        donate.save()
