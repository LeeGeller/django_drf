from rest_framework import generics

from users.models import Payments
from users.serializer import PaymentsSerializer


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
