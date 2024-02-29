from django.db import models

class Proposal(models.Model):

    STATUS_CHOICES = (
        ("Entered", "Entered"),
        ("In progress", "n progress"),
        ("Finished", "Finished"),
        ("Rejected", "Rejected"),
    )
    CATEGORY_CHOICES = (
        ("General", "General"),
        ("Classes", "Classes"),
        ("Adminstrative", "Adminstrative"),
        ("Technical", "Technical"),
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Entered")
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="General"
    )
    upvotes_count  = models.PositiveIntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    proposal = models.ForeignKey(Proposal, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Upvote(models.Model):
    proposal = models.ForeignKey(Proposal, related_name='upvotes', on_delete=models.CASCADE)
    browser_fingerprint = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
