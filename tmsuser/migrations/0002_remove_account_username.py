# Generated by Django 3.0.3 on 2020-05-28 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tmsuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
    ]
