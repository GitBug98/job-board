from django.db import models
from django.utils.text import slugify
from django import forms
from django.contrib.auth.models import User


"""
this is module 
for manage database
"""


def img_upload(instance, img_name):
    '''
    img_upload function to customize name & storge dir
    '''
    name, ext = img_name.split(".")

    return "jobs/%s.%s"%(instance.id, ext)

def cv_upload(instance, cv_name):
    '''
    img_upload function to customize name & storge dir
    '''
    name, ext = cv_name.split(".")
    # will change id to user name 
    return "cv/%s.%s"%(instance.id, ext)


JOB_TYPE = (
    ("FULL TIME", "FULL TIME"),
    ("PART TIME", "PART TIME"),
)


# Create your models here.
class Job(models.Model):

    '''
    calss for manage Job table in database
'''
    Publisher = models.ForeignKey(User, related_name=("Publisher"), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    location = models.CharField( max_length=50)
    Job_Nature = models.CharField(max_length=15, choices=JOB_TYPE)
    Published_time = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True)
    img = models.ImageField(upload_to=img_upload)

    slug = models.SlugField(null=True, blank=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Apply(models.Model):
    job = models.ForeignKey(Job, related_name="apply_job", on_delete=models.CASCADE)
    aplly_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=60)
    website = models.CharField( max_length=50)
    cv = models.FileField(upload_to=cv_upload)
    coverletter = models.TextField(max_length=100)

    def __str__(self):
        return self.name



