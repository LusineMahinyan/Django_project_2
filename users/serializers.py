from rest_framework import serializers
from .models import User, Payment
from materials.models import Course, Lesson


class CourseShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name")


class LessonShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("id", "name")


class PaymentSerializer(serializers.ModelSerializer):
    paid_course = CourseShortSerializer(read_only=True)
    paid_lesson = LessonShortSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

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


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "phone", "city")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
