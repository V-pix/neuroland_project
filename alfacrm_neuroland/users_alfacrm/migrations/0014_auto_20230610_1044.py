# Generated by Django 3.2.18 on 2023-06-10 10:44

import django.contrib.auth.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_alfacrm', '0013_auto_20230527_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alfacrmuser',
            name='firebase_token',
        ),
        migrations.AlterField(
            model_name='alfacrmuser',
            name='referral_code',
            field=models.CharField(
                blank=True,
                help_text='Реферальный код сгенерируется автоматически '
                          'после сохранения пользователя',
                max_length=10,
                unique=True,
                verbose_name='Реферальный код пользователя'
            ),
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                (
                    'id', models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                ('fcm_token', models.CharField(max_length=128)),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='tokens',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
        ),
    ]
