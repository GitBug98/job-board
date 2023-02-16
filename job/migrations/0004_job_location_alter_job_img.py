# Generated by Django 4.1.6 on 2023-02-08 13:06

from django.db import migrations, models
import job.models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='', max_length=63),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='img',
            field=models.ImageField(upload_to=job.models.img_upload),
        ),
    ]