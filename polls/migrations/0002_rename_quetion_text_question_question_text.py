# Generated by Django 4.2.20 on 2025-03-29 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quetion_text',
            new_name='question_text',
        ),
    ]
