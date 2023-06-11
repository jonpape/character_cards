# Generated by Django 4.2.2 on 2023-06-11 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("character_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="character",
            old_name="appreciated_for",
            new_name="appreciation",
        ),
        migrations.RenameField(
            model_name="character",
            old_name="skills",
            new_name="skill_1",
        ),
        migrations.AddField(
            model_name="character",
            name="skill_2",
            field=models.CharField(default="unknown", max_length=300),
        ),
        migrations.AddField(
            model_name="character",
            name="skill_3",
            field=models.CharField(default="unknown", max_length=300),
        ),
    ]
