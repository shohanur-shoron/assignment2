from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/create/', views.create_contact, name='create_contact'),
    path('contacts/<int:pk>/update/', views.update_contact, name='update_contact'),
    path('contacts/<int:pk>/delete/', views.delete_contact, name='delete_contact'),
]