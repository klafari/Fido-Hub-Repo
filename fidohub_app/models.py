from django.db import models
from django.urls import reverse

# Create your models here.
class Client(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

class Dog(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dog-detail', args=[str(self.id)])
