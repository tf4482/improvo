import hashlib
from django.db.models import F
from django.utils.encoding import smart_bytes
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from .models import Proposal, Comment, Upvote
from django.db.models import Q


def proposals(request):
    search_query = request.GET.get('search')
    if search_query:
        proposals = Proposal.objects.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )
    else:
        proposals = Proposal.objects.all()

    return render(request, "all_proposals.html", {"proposals": proposals})


@login_required
def proposal_details(request, id):
    error_message = None
    proposal = get_object_or_404(Proposal, id=id)
    comments = Comment.objects.filter(proposal=proposal)
    upvote_count = proposal.upvotes.count()

    if request.method == "POST":
        text = request.POST.get("Text")

        if text:
            author = request.user
            Comment.objects.create(author=author, text=text, proposal=proposal)
        else:
            error_message = _("Text is required!")

    return render(
        request,
        "proposal_details.html",
        {
            "proposal": proposal,
            "comments": comments,
            "error_message": error_message,
            "upvote_count": upvote_count,
        },
    )


@login_required
def proposal_submission(request):
    categories = Proposal.CATEGORY_CHOICES
    error_message = None

    if request.method == "POST":
        title = request.POST.get("Title")
        proposal_content = request.POST.get("Proposal")
        category = request.POST.get("Category")
        user = request.user

        if title and proposal_content and category:
            Proposal.objects.create(
                title=title, 
                content=proposal_content, 
                category=category,
                author=user
            )
            return redirect("home")
        else:
            error_message = _("Category, title, and/or proposal content are required.")

    return render(
        request,
        "proposal_submission.html",
        {"categories": categories, "error_message": error_message},
    )


def upvote_proposal(request, proposal_id):
    if request.method == "POST":
        proposal = get_object_or_404(Proposal, id=proposal_id)

        current_user = request.user

        if Upvote.objects.filter(
            proposal=proposal, user_id=current_user
        ).exists():
            Upvote.objects.filter(proposal=proposal, user_id=current_user).delete()
            proposal.upvotes_count = F("upvotes_count") - 1
            proposal.save()
            return redirect("proposal_details", id=proposal_id)

        else:
            proposal.upvotes_count = F("upvotes_count") + 1
            proposal.save()
            Upvote.objects.create(
                proposal=proposal, user_id=current_user
            )

        return redirect("proposal_details", id=proposal_id)


class CustomPasswordChangeDoneRedirectView(RedirectView):
    url = reverse_lazy('home')


def home(request):
    return render(request, "home.html")
