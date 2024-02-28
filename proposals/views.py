from django.http import HttpResponse
from django.template import loader
from .models import Proposal

def proposals(request):
  proposals = Proposal.objects.all().values()
  template = loader.get_template('all_proposals.html')
  context = {
    'proposals': proposals,
  }
  return HttpResponse(template.render(context, request))

def proposal_details(request, id):
  proposal = Proposal.objects.get(id=id)
  template = loader.get_template('proposal_details.html')
  context = {
    'proposal': proposal,
  }
  return HttpResponse(template.render(context, request))

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
