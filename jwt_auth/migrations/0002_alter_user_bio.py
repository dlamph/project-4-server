# Generated by Django 3.2.4 on 2021-06-21 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(max_length=3000),
        ),
    ]
