# Generated by Django 4.2 on 2024-04-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_question_question_note"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="type",
            field=models.CharField(
                choices=[("Single", "Single choose"), ("Multiple", "Multiple choose")],
                default="Single",
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_note",
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name="Note"),
        ),
    ]
