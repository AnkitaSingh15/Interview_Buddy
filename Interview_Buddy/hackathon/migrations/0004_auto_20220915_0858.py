# Generated by Django 3.2 on 2022-09-15 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0003_remove_job_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='posted_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
