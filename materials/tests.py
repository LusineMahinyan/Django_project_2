from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from materials.models import Course, Lesson, Subscription

User = get_user_model()


class APITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com",
            password="1234"
        )

        self.course = Course.objects.create(
            name="Test course",
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            name="Test lesson",
            course=self.course,
            owner=self.user,
            video_url="https://youtube.com/test"
        )



    def auth(self):
        self.client.force_authenticate(user=self.user)



    def test_course_list(self):
        self.auth()
        response = self.client.get("/api/courses/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_lesson_list(self):
        self.auth()
        response = self.client.get("/api/lessons/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_subscription_toggle(self):
        self.auth()

        url = "/api/subscribe/"
        data = {"course_id": self.course.id}

        # add
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Subscription.objects.count(), 1)

        # remove
        response = self.client.post(url, data)
        self.assertEqual(Subscription.objects.count(), 0)