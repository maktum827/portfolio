# Generated by Django 3.1.4 on 2021-11-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='users/default-avatar.png', null=True, upload_to='users/'),
        ),
    ]