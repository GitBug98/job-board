from django.shortcuts import render
from .models import Job


# Create your views here.
def job_list(request):
    job_lister = Job.objects.all()
    context = {'jobs': job_lister}
    return render(request, 'job/job_list.html', context)


def job_details(request, id):
    pass
