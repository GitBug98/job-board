from django.urls import path
from . import views
app_name = 'send_mail'

urlpatterns = [
    path('', views.send_mail, name='send_mail'),

]