# Generated by Django 4.1.3 on 2022-11-12 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies: list = []

    operations = [
        migrations.CreateModel(
            name="Analysis",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="FreeAnswer",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("value", models.TextField()),
                (
                    "analysis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fa_analysis.analysis",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Token",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.CharField(max_length=256)),
                (
                    "free_answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fa_analysis.freeanswer",
                    ),
                ),
            ],
        ),
    ]
