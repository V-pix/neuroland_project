# Generated by Django 3.2.18 on 2023-04-05 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0008_auto_20230405_1234"),
    ]

    operations = [
        migrations.CreateModel(
            name="Direction",
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
                (
                    "name",
                    models.CharField(
                        max_length=200, verbose_name="Название направления"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="course",
            name="direction",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.direction"
            ),
        ),
    ]
