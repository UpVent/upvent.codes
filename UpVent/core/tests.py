from http import HTTPStatus
from django.test import TestCase

# Test Core Pages
class CorePagesTests(TestCase):
    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about(self):
        response = self.client.get("/about/")
        response301 = self.client.get("/about")
        self.assertEqual(response301.status_code, HTTPStatus.MOVED_PERMANENTLY)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_services(self):
        response = self.client.get("/services/")
        response301 = self.client.get("/services")
        self.assertEqual(response301.status_code, HTTPStatus.MOVED_PERMANENTLY)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_licenses(self):
        response = self.client.get("/licenses/")
        response301 = self.client.get("/licenses")
        self.assertEqual(response301.status_code, HTTPStatus.MOVED_PERMANENTLY)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_ppolicy(self):
        response = self.client.get("/privacy-policy/")
        response301 = self.client.get("/privacy-policy")
        self.assertEqual(response301.status_code, HTTPStatus.MOVED_PERMANENTLY)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_tos(self):
        response = self.client.get("/terms-of-service/")
        response301 = self.client.get("/terms-of-service")
        self.assertEqual(response301.status_code, HTTPStatus.MOVED_PERMANENTLY)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_team(self):
        response = self.client.get("/team/")
        response301 = self.client.get("/team")
        self.assertEqual(response301.status_code, HTTPStatus.MOVED_PERMANENTLY)
        self.assertEqual(response.status_code, HTTPStatus.OK)

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
