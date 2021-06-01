from http import HTTPStatus
from django.test import TestCase

# Robots.txt test

class RobotsTxtTests(TestCase):
    def test_get(self):
        response = self.client.get("/robots.txt")

        self.assertEqual(response.status_code, HTTPStatus.OK)
