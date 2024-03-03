import django.shortcuts
from django.urls import path
from . import views
from .views import language_select

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
    path("upvote/<int:proposal_id>/", views.upvote_proposal, name="upvote_proposal"),
    path("select-language/", language_select, name="language_select"),
]
