# Resources
from .decorators import allowed_users
from .models import Client, Dog, DogWalker
from .forms import DogForm, CreateUserForm, ClientForm

from django.views import generic
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Index View
def index(request):

    return render( request, 'fidohub_app/index.html')

# Client List View
class ClientListView(LoginRequiredMixin, generic.ListView):

    model = Client

# Client Detail View
class ClientDetailView(LoginRequiredMixin, generic.DetailView):

    model = Client

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['dog_list'] = Dog.objects.all()
        return context

# Dog List View
class DogListView(LoginRequiredMixin, generic.ListView):

    model = Dog

# Dog Detail View
class DogDetailView(LoginRequiredMixin, generic.DetailView):

    model = Dog

# Dog Walker List View
class DogWalkerListView(generic.ListView):
    
    model = DogWalker

# Dog Walker Detail View
class DogWalkerDetailView(generic.DetailView):

    model = DogWalker

# Create Dog View
def createDog(request, client_id):

    # Initialize Variables
    form = DogForm()
    owner = Client.objects.get(pk=client_id)
    
    if request.method == 'POST':

        # Create a new dictionary with form data and portfolio_id
        dog_data = request.POST.copy()
        dog_data['client_id'] = client_id
        form = DogForm(dog_data, request.FILES)

        if form.is_valid():

            # Save the form without committing to the database
            dog = form.save(commit=False)

            # Set the portfolio relationship
            dog.owner = owner
            dog.save()

            # Redirect back to the portfolio detail page
            return redirect('client-detail', client_id)

    context = {'form': form}
    return render(request, 'fidohub_app/dog_form.html', context)

# Delete Dog View
def deleteDog(request, client_id, dog_id):

    # Initialize Variables
    dog = Dog.objects.get(pk=dog_id)

    if request.method == 'POST':

        # Delete the project and send back to portfolio details screen
        dog.delete()
        return redirect('client-detail', client_id)
    
    # Send to the project delete template
    context = {'dog': dog}
    return render(request, 'fidohub_app/dog_delete.html', context)

# Update Dog View
def updateDog(request, client_id, dog_id):

    # Initialize Variables
    dog = Dog.objects.get(pk=dog_id)
    form = DogForm(instance=dog)

    if request.method == 'POST':

        form = DogForm(request.POST, request.FILES, instance=dog)

        if form.is_valid():

            # Save the form
            dog.save()

            # Redirect back to the portfolio detail page
            return redirect('client-detail', client_id)

    # Send to the project form template 
    context = {'form': form, 'dog': dog}
    return render(request, 'fidohub_app/dog_form.html', context)

# Register View
def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='client_role')
            user.groups.add(group)

            client = Client.objects.create(user=user)
            client.name = username
            client.email = form.cleaned_data.get('email')
            client.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        
    context={'form':form}
    return render(request, 'registration/register.html', context)


# User Page View
@login_required(login_url='login')
@allowed_users(allowed_roles=['client_role'])
def userPage(request):

    client = request.user.client
    form = ClientForm(instance= client)
    print('client', client)

    if request.method == 'POST':

        form = ClientForm(request.POST, request.FILES, instance=client)

        if form.is_valid():

            form.save()

    context = {'form':form}
    return render(request, 'fidohub_app/user.html', context)

'''
@login_required(login_url='login')
@allowed_users(allowed_roles=['client_role'])
'''