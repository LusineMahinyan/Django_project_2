from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import User, Payment
from .serializers import UserSerializer, PaymentSerializer, RegisterSerializer
from .services.stripe_service import (
    create_product,
    create_price,
    create_session
)


# -------------------------
# REGISTRATION
# -------------------------
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# -------------------------
# USERS
# -------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# -------------------------
# PAYMENTS
# -------------------------
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)

        name = (
            payment.paid_course.name
            if payment.paid_course
            else payment.paid_lesson.name
        )

        amount = int(payment.amount * 100)

        product = create_product(name)
        price = create_price(product.id, amount)
        session = create_session(price.id)

        payment.stripe_product_id = product.id
        payment.stripe_price_id = price.id
        payment.stripe_session_id = session.id
        payment.payment_link = session.url
        payment.save()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
