# Generated by Django 5.0.2 on 2024-02-29 02:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0005_proposal_upvotes_count_upvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='upvote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
