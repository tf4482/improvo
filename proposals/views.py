from django.shortcuts import render, redirect
from django.template import loader
from .models import Proposal

def proposals(request):
    proposals = Proposal.objects.all()
    return render(request, 'all_proposals.html', {'proposals': proposals})

def proposal_details(request, id):
    proposal = Proposal.objects.get(id=id)
    return render(request, 'proposal_details.html', {'proposal': proposal})

def index(request):
    return render(request, 'index.html')
