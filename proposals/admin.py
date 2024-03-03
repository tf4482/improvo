from django.contrib import admin
from .models import Proposal, Comment, Upvote

admin.site.register(Proposal)
admin.site.register(Comment)
admin.site.register(Upvote)
