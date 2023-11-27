# Resources
from .models import Dog, Client

from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Dog Form
class DogForm(ModelForm):

    class Meta:

        model = Dog
        fields =('name', 'breed', 'age', 'about', 'dog_image')

# Client Form
class ClientForm(ModelForm):

    class Meta:

        model = Client
        fields = '__all__'
        exclude = ['user']

# Create User Form
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        exclude = ['group']