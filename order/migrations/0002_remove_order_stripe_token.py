# Generated by Django 5.0.7 on 2024-07-24 19:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="stripe_token",
        ),
    ]
