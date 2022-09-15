# Generated by Django 3.2 on 2022-09-15 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0005_alter_job_job_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCandidateMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.candidate')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.job')),
            ],
            options={
                'unique_together': {('job_id', 'candidate')},
            },
        ),
    ]
