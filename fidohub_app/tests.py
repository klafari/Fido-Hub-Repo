from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Dog, Client


# Create your tests here.

# SimpleTestCase
class indexTests(SimpleTestCase):

    def test_index_available_by_namespace(self):  
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_template_name(self):  
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "fidohub_app/index.html")

    def test_index_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<h1>welcome to fidohub!</h1>")
        self.assertNotContains(response, "goodbye!")

# TestCase
class DogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.dog = Dog.objects.create(name="Max", breed="Yorkie", owner=Client.objects.create(name="Amy", email="amy@gmail.com"))

    def test_dog_content(self):
        self.assertEqual(self.dog.name, "Max")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/dogs/")
        self.assertEqual(response.status_code, 200)

