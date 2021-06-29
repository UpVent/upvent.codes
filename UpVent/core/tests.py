from http import HTTPStatus
from django.test import TestCase

# Robots.txt test
class RobotsTxtTests(TestCase):
    def test_get(self):
        response = self.client.get("/robots.txt")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response["content-type"], "text/plain")
        lines = response.content.decode().splitlines()
        self.assertEqual(lines[0], "Sitemap: https://upvent.codes/sitemap.xml")
        self.assertEqual(lines[1], "User-Agent: *")

    def test_post_disallowed(self):
        response = self.client.post("/robots.txt")

        self.assertEqual(HTTPStatus.METHOD_NOT_ALLOWED, response.status_code)

# sitemap.xml test
class SitemapTests(TestCase):
    def test_sitemap(self):
        response = self.client.get("/sitemap.xml")

        self.assertEqual(response.status_code, HTTPStatus.OK)
