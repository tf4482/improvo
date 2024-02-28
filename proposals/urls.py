from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("proposals/", views.proposals, name="proposals"),
    path(
        "proposals/proposal_submission",
        views.proposal_submission,
        name="proposal_submission",
    ),
    path(
        "proposals/proposal_details/<int:id>",
        views.proposal_details,
        name="proposal_details",
    ),
]
