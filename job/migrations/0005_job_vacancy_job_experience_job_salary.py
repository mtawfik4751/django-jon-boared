# Generated by Django 4.2.1 on 2023-05-11 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]