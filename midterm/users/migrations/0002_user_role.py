# Generated by Django 3.1.7 on 2021-03-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Guest')], default=2),
        ),
    ]