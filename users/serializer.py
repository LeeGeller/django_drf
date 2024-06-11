from rest_framework import serializers

from users.models import Payments


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        exclude = ("created_ad",)
