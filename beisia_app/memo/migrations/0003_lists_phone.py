# Generated by Django 3.0.5 on 2020-11-20 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0002_lists_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lists',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
