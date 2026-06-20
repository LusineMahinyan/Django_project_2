from rest_framework import viewsets, generics

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from .tasks import send_course_update_email


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_update(self, serializer):
        course = serializer.save()
        send_course_update_email.delay(course.id)


class LessonListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        queryset = Lesson.objects.all()
        course_id = self.request.query_params.get("course")

        if course_id:
            queryset = queryset.filter(course_id=course_id)

        return queryset


class LessonRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
