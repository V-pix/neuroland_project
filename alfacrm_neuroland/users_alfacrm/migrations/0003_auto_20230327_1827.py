# Generated by Django 3.2.18 on 2023-03-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users_alfacrm", "0002_auto_20230325_1337"),
    ]

    operations = [
        migrations.AddField(
            model_name="alfacrmuser",
            name="balance",
            field=models.IntegerField(default=0),
        ),
    ]
