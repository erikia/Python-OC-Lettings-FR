from django.urls import reverse
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from .models import Profile
from .views import profiles_index, profile


class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user1 = User.objects.create(username="testuser1")
        self.user2 = User.objects.create(username="testuser2")
        self.profile1 = Profile.objects.create(user=self.user1)
        self.profile2 = Profile.objects.create(user=self.user2)

    def test_profiles_index(self):
        url = reverse("index")
        request = self.factory.get(url)
        response = profiles_index(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.profile1.__str__(), response.content.decode())
        self.assertIn(self.profile2.__str__(), response.content.decode())
        self.assertIn("<title>", response.content.decode())

    def test_profile(self):
        url = reverse("profiles:profile", args=["testuser1"])
        request = self.factory.get(url)
        response = profile(request, username="testuser1")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.profile1.user.username, str(response.content))
        self.assertIn("<title>", str(response.content))
