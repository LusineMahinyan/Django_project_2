from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from materials.models import Course, Lesson


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com",
            password="12345"
        )

        self.course = Course.objects.create(
            name="Python"
        )

        self.lesson = Lesson.objects.create(
            name="Lesson 1",
            course=self.course,
            video_url="https://youtube.com/watch?v=test"
        )

        self.client.force_authenticate(user=self.user)

    def test_list_lessons(self):
        response = self.client.get("/api/lessons/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        data = {
            "name": "Lesson 2",
            "course": self.course.id,
            "video_url": "https://youtube.com/watch?v=test2"
        }

        response = self.client.post(
            "/api/lessons/",
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_lesson(self):
        response = self.client.patch(
            f"/api/lessons/{self.lesson.id}/",
            {"name": "Updated lesson"}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.lesson.refresh_from_db()

        self.assertEqual(
            self.lesson.name,
            "Updated lesson"
        )

    def test_delete_lesson(self):
        response = self.client.delete(
            f"/api/lessons/{self.lesson.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
