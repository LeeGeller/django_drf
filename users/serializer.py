from rest_framework import serializers

from materials.models import Course
from users.models import Payments, User


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
