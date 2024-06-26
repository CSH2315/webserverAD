# Generated by Django 4.2 on 2024-06-06 09:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pybo", "0006_question_hits"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="voter_negative",
            field=models.ManyToManyField(
                related_name="voter_answer_nega", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="voter_negative",
            field=models.ManyToManyField(
                related_name="voter_question_nega", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
