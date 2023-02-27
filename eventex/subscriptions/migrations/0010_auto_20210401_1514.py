# Generated by Django 3.1.6 on 2021-04-01 18:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0009_auto_20210401_1420"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("eeb9759d-19ce-47ed-8226-3134024c8b63"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
