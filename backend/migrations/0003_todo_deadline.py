# Generated by Django 4.1.3 on 2022-11-03 13:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_todo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
