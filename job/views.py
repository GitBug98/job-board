from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .form import Addform, ApplyForm 

# https://docs.djangoproject.com/en/4.1/ref/models/querysets/  # querysets docs

# Create your views here.
'''
job_lister function return all jobs to html page "job_list.html"
'''


def job_lister(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj}
    return render(request, 'job/job_list.html', context)


'''
job_details function return selected job to html page "job_details.html"
'''


def job_details(request, slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ApplyForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            my_form = form.save(commit=False)
            # select job for apply
            my_form.job = job_detail
            my_form.save()
            # redirect to a new URL:
            # will add aplly done page later
        
    else:
        form = ApplyForm
    context = {'job': job_detail, 'form':form}
    return render(request, 'job/job_details.html', context)


def add_job(request):
    if request.method == 'POST':
        form = Addform(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.Publisher = request.user
            my_form.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = Addform
    
    return render(request, 'job/add_job.html', {'addform':form})