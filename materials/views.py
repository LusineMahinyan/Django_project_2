from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Course, Lesson, Subscription
from .serializers import CourseSerializer, LessonSerializer
from users.permissions import IsOwner

from .paginators import CoursePagination, LessonPagination




class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.groups.filter(name="moderator").exists():
            return Course.objects.all()

        return Course.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]

        return [IsAuthenticated()]



class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = LessonPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.groups.filter(name="moderator").exists():
            return Lesson.objects.all()

        return Lesson.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]

        return [IsAuthenticated()]



class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        course_id = request.data.get("course_id")

        course = get_object_or_404(Course, id=course_id)

        subscription = Subscription.objects.filter(
            user=user,
            course=course
        )

        if subscription.exists():
            subscription.delete()
            message = "подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course)
            message = "подписка добавлена"

        return Response({"message": message})
