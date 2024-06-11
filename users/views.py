from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from users.models import Payments
from users.serializer import PaymentsSerializer


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_fields = (
        "cash",
        "transfer_to_account",
        "courses",
        "lessons",
    )
    ordering_fields = ("date_of_payment",)
