# Generated by Django 3.2.18 on 2023-04-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0011_video_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="direction",
            options={
                "verbose_name": "Направление",
                "verbose_name_plural": "Направления",
            },
        ),
        migrations.AddField(
            model_name="direction",
            name="about_direction",
            field=models.TextField(
                default=1,
                help_text="Укажите описание направления",
                verbose_name="Описание направления",
            ),
            preserve_default=False,
        ),
    ]
