from django.contrib import admin
from django.views.generic.base import TemplateView
from django.urls import path, include
from django.urls import path
from . import views
from .views import language_select

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
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
