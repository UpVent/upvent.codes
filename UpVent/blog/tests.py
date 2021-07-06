import tempfile
from http import HTTPStatus
from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Post

# Test blog urls
class MainBlogPageTest(TestCase):
    def test_home(self):
        response = self.client.get("/blog/")
        response301 = self.client.get("/about")
        self.assertEqual(response301.status_code, HTTPStatus.MOVED_PERMANENTLY)
        self.assertEqual(response.status_code, HTTPStatus.OK)


# Test blog model creation

class ModelCreation(TestCase):
    def test_add_blog(self):
        author = User(username="Test User")
        newblog = Post()
        newblog.title = "TestBlog"
        newblog.STATUS = 1
        newblog.description = "Test Description"
        newblog.image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        newblog.category = "TestCat"
        newblog.slug = "test-slug"
        newblog.author = author
        newblog.content = "Cosas"
        newblog.updated_on
        newblog.created_on
