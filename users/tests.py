from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from fixtures.load_fixture import load_fixture
from materials.models import Course, Subscription
from users.models import User


class CourseTestCases(APITestCase):
    fixtures = [
        "fixtures/courses_test.json",
        "fixtures/users_test.json",
        "fixtures/subscriptions_test.json",
        "fixtures/group_test.json",
    ]

    def setUp(self):
        self.client = APIClient()
        self.manager = User.objects.get(pk=2)
        self.client.force_authenticate(user=self.manager)
        self.course1 = Course.objects.get(pk=1)
        self.course2 = Course.objects.get(pk=2)
        self.subscription1 = Subscription.objects.get(pk=1)
        self.subscription2 = Subscription.objects.get(pk=2)

    @load_fixture("fixtures/courses_test.json")
    def test_course_list(self, fixture_data):
        url = reverse("materials:course-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        actual_data = [
            {"pk": item["id"], "title_course": item["title_course"]}
            for item in response.data["results"]
        ]

        expected_data = [
            {"pk": item["pk"], "title_course": item["fields"]["title_course"]}
            for item in fixture_data
        ]

        self.assertEqual(actual_data, expected_data)

    @load_fixture("fixtures/courses_test.json")
    def test_retrieve_course(self, fixture_data):
        url = reverse("materials:course-detail", args=[self.course2.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        actual_data = {
            "pk": response.data["id"],
            "title_course": response.data["title_course"],
        }

        expected_data = {
            "pk": self.course2.pk,
            "title_course": Course.objects.get(pk=self.course2.pk).title_course,
        }

        self.assertEqual(actual_data, expected_data)

    def test_delete_course(self):
        url = reverse("materials:course-detail", args=[self.course2.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_course(self):
        url = reverse("materials:course-list")
        data = {
            "title_course": "Python для начинающих",
            "link_to_video_course": "https://www.youtube.com/watch?v=ghijkl",
            "description_course": "Описание курса для начинающих по Python",
        }
        self.client.force_authenticate(user=self.manager)
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_course(self):
        url = reverse("materials:course-detail", args=[self.course1.pk])
        data = {
            "title_course": "Python для начинающих ИЗМЕНЕННЫЙ",
            "link_to_video_course": "https://www.youtube.com/watch?v=ghijkl",
            "description_course": "Описание курса для начинающих по Python",
        }
        self.client.force_authenticate(user=self.manager)
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data_title = data["title_course"]
        actual_title = response.data["title_course"]
        self.assertEqual(data_title, actual_title)
