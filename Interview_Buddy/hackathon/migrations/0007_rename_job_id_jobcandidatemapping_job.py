# Generated by Django 3.2 on 2022-09-15 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0006_jobcandidatemapping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobcandidatemapping',
            old_name='job_id',
            new_name='job',
        ),
    ]
