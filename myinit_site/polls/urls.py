from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]  # we are naming it as index so that we can reference to this with this name later
