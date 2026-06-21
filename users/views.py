from rest_framework import generics, viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)
from rest_framework.response import Response
from rest_framework.decorators import action
import stripe

from .models import User, Payment
from .serializers import (
    UserSerializer,
    PaymentSerializer,
    RegisterSerializer,
)
from .services.stripe_service import (
    create_product,
    create_price,
    create_session,
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
    queryset = Payment.objects.all()   # <-- ВОТ ЭТО ДОБАВИТЬ
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Payment.objects.all()

        return Payment.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        payment = serializer.save(
            user=self.request.user
        )

        name = (
            payment.course.name
            if payment.course
            else payment.lesson.name
        )

        amount = int(payment.amount * 100)

        product = create_product(name)
        price = create_price(
            product.id,
            amount
        )
        session = create_session(price.id)

        payment.stripe_product_id = product.id
        payment.stripe_price_id = price.id
        payment.stripe_session_id = session.id
        payment.payment_link = session.url
        payment.save()

    @action(
        detail=True,
        methods=["get"]
    )
    def status(self, request, pk=None):
        payment = self.get_object()

        session = stripe.checkout.Session.retrieve(
            payment.stripe_session_id
        )

        payment.status = session.payment_status
        payment.save()

        return Response(
            {
                "status": payment.status,
                "payment_link": payment.payment_link,
            }
        )
