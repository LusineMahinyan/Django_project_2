from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.groups.filter(name="moderator").exists():
            return Course.objects.all()

        return Course.objects.filter(owner=user)

    def get_permissions(self):
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_destroy(self, instance):
        if (
            self.request.user.groups.filter(name="moderator").exists()
            and not self.request.user.is_superuser
        ):
            raise PermissionDenied("Модератор не может удалять курсы.")
        instance.delete()


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.groups.filter(name="moderator").exists():
            return Lesson.objects.all()

        return Lesson.objects.filter(owner=user)

    def get_permissions(self):
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_destroy(self, instance):
        if (
            self.request.user.groups.filter(name="moderator").exists()
            and not self.request.user.is_superuser
        ):
            raise PermissionDenied("Модератор не может удалять уроки.")
        instance.delete()
