# Generated by Django 4.1.6 on 2023-02-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='img',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
