# Generated by Django 3.1.4 on 2021-11-16 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AddField(
            model_name='contact',
            name='csno',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
    ]
