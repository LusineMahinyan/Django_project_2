from django.db import models
from django.conf import settings


class Course(models.Model):
    name = models.CharField(max_length=255)
    preview = models.ImageField(upload_to='course_previews/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="courses"
    )

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons'
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    preview = models.ImageField(upload_to='lesson_previews/', blank=True, null=True)
    video_url = models.URLField()

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="lessons"
    )

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="subscriptions"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subscriptions"
    )

    class Meta:
        unique_together = ("user", "course")

    def __str__(self):
        return f"{self.user} -> {self.course}"
