# Generated by Django 4.2.2 on 2024-06-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_subscription",
            field=models.BooleanField(default=False, verbose_name="Подписка"),
        ),
    ]
