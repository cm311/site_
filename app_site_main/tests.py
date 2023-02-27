from django.test import TestCase
from .models import *

class URLEndPointTest(TestCase):
    def setUp(self):
        pass

    def test_url_index_exists(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create()
        pass
    def test_thing(self):
        pass