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
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="Entered")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default = "General")
    datetime = models.DateTimeField(auto_now_add=True)
