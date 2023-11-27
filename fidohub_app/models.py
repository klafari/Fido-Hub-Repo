# Resources
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Client Model
class Client(models.Model):

    # Client Variables
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    # Client User
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    # Client Functions
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])
    
# DogWalker Model
class DogWalker(models.Model):

    # DogWalker Variables
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    about = models.CharField(max_length=200, blank=False)

    # Dog Walker Functions
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("dogwalker-detail", args=[str(self.id)])
    
# Dog Model
class Dog(models.Model):

    # Dog Variables
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    about = models.CharField(max_length=200, blank=True)

    # Dog Owner
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, default = None)

    # Dog Image
    dog_image = models.ImageField(upload_to='images/', null=True, blank=True)

    # Dog Functions
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dog-detail', args=[str(self.id)])
