# Generated by Django 4.0.5 on 2022-06-18 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_activity_options_activity_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={},
        ),
        migrations.RemoveField(
            model_name='activity',
            name='create',
        ),
    ]
