# Generated by Django 2.1.7 on 2019-02-15 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='address',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='signup',
            name='country',
            field=models.TextField(default='', max_length=200),
        ),
    ]
