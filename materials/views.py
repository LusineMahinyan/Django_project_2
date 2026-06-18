from rest_framework import viewsets
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name="moderator").exists():
            return Course.objects.all()

        return Course.objects.filter(owner=user)

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            return [IsAuthenticated(), ~IsModerator()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name="moderator").exists():
            return Lesson.objects.all()

        return Lesson.objects.filter(owner=user)

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            return [IsAuthenticated(), ~IsModerator()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)