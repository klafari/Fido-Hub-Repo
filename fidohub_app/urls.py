# Resources
from . import views

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# URL Patterns
urlpatterns = [

    # Index URL
    path('', views.index, name='index'),

    # Client URLs
    path('clients/', views.ClientListView.as_view(), name='clients'),
    path('client/<int:pk>', views.ClientDetailView.as_view(), name='client-detail'),

    # Dog URLs
    path('dogs/', views.DogListView.as_view(), name='dogs'),
    path('dog/<int:pk>', views.DogDetailView.as_view(), name='dog-detail'),

    # Dog Walker URLs
    path('dogwalkers/', views.DogWalkerListView.as_view(), name='dogwalkers'),
    path('dogwalker/<int:pk>', views.DogWalkerDetailView.as_view(), name ='dogwalker-detail'),

    # Dog Create, Delete, & Update URLs
    path('client/<int:client_id>/create_dog/', views.createDog, name='create-dog'),
    path('client/<int:client_id>/delete_dog/<int:dog_id>', views.deleteDog, name='delete-dog'),
    path('client/<int:client_id>/update_dog/<int:dog_id>', views.updateDog, name='update-dog'),

    # Account URLs
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name= 'register-page'),
    path('user/', views.userPage, name='user-page'),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)