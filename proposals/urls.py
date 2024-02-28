from django.urls import path
from . import views

urlpatterns = [
    path('proposals/', views.proposals, name='proposals'),
]
