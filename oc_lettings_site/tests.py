from django.urls import reverse
from django.test import RequestFactory, TestCase
from .views import index

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_index(self):
        url = reverse("index")
        request = self.factory.get(url)
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn("<title>", str(response.content))
