from django.contrib import admin
from django import forms
from django.utils.translation import gettext as _
from .models import Proposal, Comment, Upvote

class ProposalAdminForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = '__all__'

class ProposalAdmin(admin.ModelAdmin):
    form = ProposalAdminForm
    list_display = ['title', 'author', 'status', 'category']
    list_filter = ['status', 'category']
    search_fields = ['title', 'author']
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'content', 'status', 'category')
        }),
        (_('Advanced Options'), {
            'classes': ('collapse',),
            'fields': ('upvotes_count',),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'author', 'content', 'status', 'category'),
        }),
    )

admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Comment)
admin.site.register(Upvote)
