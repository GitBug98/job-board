# Generated by Django 4.1.6 on 2023-02-13 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aplly_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('website', models.CharField(max_length=50)),
                ('cv', models.FileField(upload_to='cv/')),
                ('coverletter', models.TextField(max_length=100)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='job.job')),
            ],
        ),
    ]
