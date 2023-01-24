# from django.urls import reverse
# from django.test import RequestFactory, TestCase
# from .models import Letting
# from .views import lettings_index, letting

# from .models import Letting, Address

# class LettingViewTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.address1 = Address.objects.create(address="123 Main St.")
#         self.address2 = Address.objects.create(address="456 Market St.")
#         self.letting1 = Letting.objects.create(
#             title="Test Letting 1", address=self.address1)
#         self.letting2 = Letting.objects.create(
#             title="Test Letting 2", address=self.address2)


#     def test_lettings_index(self):
#         url = reverse("lettings:index")
#         request = self.factory.get(url)
#         response = lettings_index(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("Test Letting 1", str(response.content))
#         self.assertIn("Test Letting 2", str(response.content))
#         self.assertIn("<title>", str(response.content))

#     def test_letting(self):
#         url = reverse("lettings:letting", args=[1])
#         request = self.factory.get(url)
#         response = letting(request, letting_id=1)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.context["title"], self.letting1.title)
#         self.assertEqual(response.context["address"], self.letting1.address)
#         self.assertIn("<title>", str(response.content))


from django.urls import reverse
from django.test import RequestFactory, TestCase
from .models import Letting, Address
from .views import lettings_index, letting


class LettingViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.address1 = Address.objects.create(
            number=123, street="Main St.", city="Springfield", state="IL",
            zip_code=12345, country_iso_code="USA")
        self.address2 = Address.objects.create(
            number=456, street="Market St.", city="Springfield", state="IL",
            zip_code=12345, country_iso_code="USA")
        self.letting1 = Letting.objects.create(
            title="Test Letting 1", address=self.address1
        )
        self.letting2 = Letting.objects.create(
            title="Test Letting 2", address=self.address2
        )

    def test_lettings_index(self):
        url = reverse("index")
        request = self.factory.get(url)
        response = lettings_index(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Letting 1", str(response.content))
        self.assertIn("Test Letting 2", str(response.content))
        self.assertIn("<title>", str(response.content))

    def test_letting(self):
        url = reverse("lettings:letting", args=[1])
        request = self.factory.get(url)
        response = letting(request, letting_id=1)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.letting1.title, str(response.content))
        self.assertIn(str(self.letting1.address), str(response.content))
        self.assertIn("<title>", str(response.content))
        self.assertIn("<h1>", str(response.content))
