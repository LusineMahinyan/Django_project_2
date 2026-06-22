from rest_framework import serializers

from .models import Course, Lesson, Subscription
from .validators import validate_youtube_url



class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[validate_youtube_url])

    class Meta:
        model = Lesson
        fields = (
            "id",
            "name",
            "description",
            "preview",
            "video_url",
            "course",
        )



class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "preview",
            "description",
            "owner",
            "lessons",
            "lessons_count",
            "is_subscribed",
        )

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        user = self.context["request"].user

        if user.is_anonymous:
            return False

        return Subscription.objects.filter(
            user=user,
            course=obj
        ).exists()
