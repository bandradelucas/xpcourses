# Generated by Django 2.2.13 on 2021-05-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
