# Generated by Django 3.2 on 2021-04-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qstion',
            name='tags',
        ),
        migrations.AddField(
            model_name='qstion',
            name='tag',
            field=models.ManyToManyField(to='app.Tags'),
        ),
    ]
