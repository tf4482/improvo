from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class Proposal(models.Model):

    STATUS_CHOICES = (
        (_("Entered"), _("Entered")),
        (_("In progress"), _("In progress")),
        (_("Finished"), _("Finished")),
        (_("Rejected"), _("Rejected")),
    )
    CATEGORY_CHOICES = (
        (_("General"), _("General")),
        (_("Classes"), _("Classes")),
        (_("Adminstrative"), _("Adminstrative")),
        (_("Technical"), _("Technical")),
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=_("Entered")
    )
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default=_("General")
    )
    upvotes_count = models.PositiveIntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='proposals', on_delete=models.CASCADE)

    @property
    def upvote_count(self):
        return self.upvotes.count()

    upvote_count_db = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            return

        self.upvote_count_db = self.upvotes.count()
        super().save(*args, **kwargs)


class Comment(models.Model):
    proposal = models.ForeignKey(
        Proposal, related_name="comments", on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Upvote(models.Model):
    proposal = models.ForeignKey(
        Proposal, related_name="upvotes", on_delete=models.CASCADE
    )
    user_id = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
