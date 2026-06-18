from rest_framework import serializers
from .models import User, Payment


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "phone", "city", "avatar"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"