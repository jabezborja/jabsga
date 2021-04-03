from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .models import Url
from .forms import NewUrlForm

class UrlTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="admin")
        Url.objects.create(title="Test", urlName="Test", url="test")

    def test_post_is_posted(self):
        """URLs are created"""
        post1 = Url.objects.get(title="Test")
        self.assertEqual(post1.title, "We are testing this")

    def test_valid_form_data(self):
        form = Url({
            'title': "Just testing",
            'url': "Repeated tests make the app foul-proof",
        })
        self.assertTrue(form.is_valid())
        post1 = form.save(commit=False)
        post1.author = self.user1
        post1.save()
        self.assertEqual(post1.title, "Just testing")
        self.assertEqual(post1.text, "Repeated tests make the app foul-proof")

    def test_blank_form_data(self):
        form = NewUrlForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'title': ['This field is required.'],
            'text': ['This field is required.'],
        })
