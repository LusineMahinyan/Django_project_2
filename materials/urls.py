from django.urls import path
from .views import SubscriptionAPIView

urlpatterns = [
    path("subscribe/", SubscriptionAPIView.as_view()),
]
