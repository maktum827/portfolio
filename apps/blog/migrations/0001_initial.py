# Generated by Django 3.1.4 on 2021-11-16 12:06

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=500)),
                ('category', models.CharField(default='', max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('author_name', models.CharField(default='', max_length=500)),
                ('desc', tinymce.models.HTMLField()),
                ('prgmngImg', models.ImageField(blank=True, default='Programming.png', null=True, upload_to='images/')),
            ],
        ),
    ]
