from django.shortcuts import render
from .models import Information
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.




def send_mail(request):
    info = Information.objects.first
    if request.method == 'POST':
        Subject = request.POST['Subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            Subject,
            message,
            settings.EMAIL_HOST_USER,
            email,
           
        )

    return render(request, 'contact/contact.html', {'info':info})
