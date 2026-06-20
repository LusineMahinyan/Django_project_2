from rest_framework import serializers
from .models import User, Payment
from materials.models import Course, Lesson


class CoursePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name")


class LessonPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("id", "name")


class PaymentSerializer(serializers.ModelSerializer):
    paid_course = CoursePaymentSerializer(read_only=True)
    paid_lesson = LessonPaymentSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "phone",
            "city",
            "avatar",
            "payments",
        )
