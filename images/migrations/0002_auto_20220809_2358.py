# Generated by Django 3.0.14 on 2022-08-09 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
