from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.ClientListView.as_view(), name= 'clients'),
    path('client/<int:pk>', views.ClientDetailView.as_view(), name='client-detail'),
    path('dogs/', views.DogListView.as_view(), name= 'dogs'),
    path('dog/<int:pk>', views.DogDetailView.as_view(), name= 'dog-detail'),
    path('client/<int:client_id>/create_dog/', views.createDog, name='create-dog'),
    path('client/<int:client_id>/delete_dog/<int:dog_id>', views.deleteDog, name='delete-dog'),
    path('client/<int:client_id>/update_dog/<int:dog_id>', views.updateDog, name='update-dog'),
    path('accounts/', include('django.contrib.auth.urls'))
]
