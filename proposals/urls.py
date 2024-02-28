from django.urls import path
from . import views

urlpatterns = [
    path('proposals/', views.members, name='proposals'),
]
