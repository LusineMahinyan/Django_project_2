from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import User, Payment
from .serializers import RegisterSerializer, PaymentSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Payment.objects.all()

        course = self.request.query_params.get("course")
        lesson = self.request.query_params.get("lesson")
        method = self.request.query_params.get("method")
        ordering = self.request.query_params.get("ordering")

        if course:
            queryset = queryset.filter(course_id=course)

        if lesson:
            queryset = queryset.filter(lesson_id=lesson)

        if method:
            queryset = queryset.filter(method=method)

        if ordering == "date":
            queryset = queryset.order_by("date")
        elif ordering == "-date":
            queryset = queryset.order_by("-date")

        return queryset
