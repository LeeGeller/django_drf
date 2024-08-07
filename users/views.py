from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from users.models import Payments, User
from users.serializer import PaymentsSerializer, UserCreateSerializer
from users.services import create_donation


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_fields = (
        "courses",
        "lessons",
    )
    ordering_fields = ("date_of_payment",)


class PaymentsCreateAPIView(generics.CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):

        payments = serializer.save(user=self.request.user)
        validated_data = serializer.validated_data

        if validated_data.get("course"):

            product_id, price = validated_data.get("course"), validated_data.get(
                "sum_of_payment"
            )
        elif validated_data.get("lesson"):
            product_id, price = validated_data.get("lesson"), validated_data.get(
                "sum_of_payment"
            )

        stripe_id, session_id, donate_url = create_donation(
            product_id, self.request.user, price
        )

        payments.donate_url = donate_url
        payments.session_id = session_id
        payments.save()


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
