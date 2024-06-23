from rest_framework import serializers

from donations.models import Donate


class DonateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donate
        exclude = ("created_at",)
