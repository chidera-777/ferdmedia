# Generated by Django 3.0.14 on 2022-08-09 22:20

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('ferdmedia', '0002_profile_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.jpg', force_format='JPEG', keep_meta=True, quality=95, scale=0.5, size=[1042, 1099], upload_to='users/%Y/%m/%d'),
        ),
    ]