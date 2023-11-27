# Resources
from .models import Dog, Client

from django.test import TestCase, SimpleTestCase, LiveServerTestCase
from django.urls import reverse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
        self.assertContains(response, "<h1>Welcome to FidoHub!</h1>")
        self.assertNotContains(response, "goodbye!")

# TestCase
class DogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.dog = Dog.objects.create(name="Max", breed="Yorkie", owner=Client.objects.create(name="Amy", email="amy@gmail.com"))

    def test_dog_content(self):
        self.assertEqual(self.dog.name, "Max")

# Selenium
'''
class DogFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()

    selenium.get('http://127.0.0.1:8000/client/4/create_dog/')

    dog_name = selenium.find_element_by_id('id_name')
    dog_breed = selenium.find_element_by_id('id_breed')
    dog_age = selenium.find_element_by_id('id_age')
    submit = selenium.find_element_by_id('submit_button')

    dog_name.send_keys('Max')
    dog_breed.send_keys('Poodle')
    dog_age.send_keys('5')

    submit.send_keys(Keys.RETURN)
    assert 'Max' in selenium.page_source
'''