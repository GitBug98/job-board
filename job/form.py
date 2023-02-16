from django import forms

from .models import Apply,Job

class ApplyForm(forms.ModelForm):
    class Meta:
       model = Apply
       fields = ['name', 'email', 'website', 'cv', 'coverletter']

class Addform(forms.ModelForm):
    class Meta:
       model = Job
       fields = '__all__'
       exclude = 'slug','Publisher',