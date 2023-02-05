from django.db import models

JOB_TYPE = (
    ("FULL TIME", "FULL TIME"),
    ("PART TIME", "PART TIME"),
)


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=50)
    # location
    Job_Nature = models.CharField(max_length=15, choices=JOB_TYPE)
    Published_time = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
