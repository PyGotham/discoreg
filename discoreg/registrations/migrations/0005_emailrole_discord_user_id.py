# Generated by Django 3.0.8 on 2020-07-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registrations", "0004_auto_20200720_0524"),
    ]

    operations = [
        migrations.AddField(
            model_name="emailrole",
            name="discord_user_id",
            field=models.CharField(default=None, max_length=32, null=True),
        ),
    ]
