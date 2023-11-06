from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views import generic
from .models import Client, Dog
from .forms import DogForm

# Create your views here.
def index(request):
    return render( request, 'fidohub_app/index.html')

class ClientListView(generic.ListView):
    model = Client
class ClientDetailView(generic.DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dog_list'] = Dog.objects.all()
        return context

class DogListView(generic.ListView):
    model = Dog
class DogDetailView(generic.DetailView):
    model = Dog

def createDog(request, client_id):
    # Initialize Variables
    form = DogForm()
    owner = Client.objects.get(pk=client_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        dog_data = request.POST.copy()
        dog_data['client_id'] = client_id
        
        form = DogForm(dog_data)
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

def updateDog(request, client_id, dog_id):
    # Initialize Variables
    dog = Dog.objects.get(pk=dog_id)
    form = DogForm(instance=dog)

    if request.method == 'POST':
        form = DogForm(request.POST, instance=dog)
        if form.is_valid():
            # Save the form
            dog.save()
            # Redirect back to the portfolio detail page
            return redirect('client-detail', client_id)

    # Send to the project form template 
    context = {'form': form, 'dog': dog}
    return render(request, 'fidohub_app/dog_form.html', context)