from django.shortcuts import render, redirect, get_object_or_404

from .models import Proposal
from .models import Comment


def proposals(request):
    proposals = Proposal.objects.all()
    return render(request, "all_proposals.html", {"proposals": proposals})


def proposal_details(request, id):
    error_message = None
    proposal = Proposal.objects.get(id=id)
    comments = Comment.objects.filter(proposal=proposal)

    if request.method == "POST":
        author = request.POST.get("Author")
        text = request.POST.get("Text")

        if author and text:
            proposal = get_object_or_404(Proposal, id=id)
            Comment.objects.create(author=author, text=text, proposal=proposal)
        else:
            error_message = "Author and/or text required!"

    return render(
        request,
        "proposal_details.html",
        {"proposal": proposal, "comments": comments, "error_message": error_message},
    )


def proposal_submission(request):
    categories = Proposal.CATEGORY_CHOICES
    error_message = None

    if request.method == "POST":
        title = request.POST.get("Title")
        proposal_content = request.POST.get("Proposal")
        category = request.POST.get("Category")

        if title and proposal_content and category:
            Proposal.objects.create(
                title=title, content=proposal_content, category=category
            )
            return redirect("index")
        else:
            error_message = "Category, title, and/or proposal content are required."

    return render(
        request,
        "proposal_submission.html",
        {"categories": categories, "error_message": error_message},
    )


def index(request):
    return render(request, "index.html")
