from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="homepage"),
    path('contact', contact, name='contact_me')
]