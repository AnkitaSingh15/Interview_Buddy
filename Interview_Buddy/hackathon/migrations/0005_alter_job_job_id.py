# Generated by Django 3.2 on 2022-09-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0004_auto_20220915_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_id',
            field=models.TextField(unique=True),
        ),
    ]