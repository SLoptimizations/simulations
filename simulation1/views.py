from django.shortcuts import render
import uuid
# from . models import UserInfo
from django.views.generic import TemplateView, CreateView, View
from . funcs.main import send_mail
from django.contrib.auth.models import User


# Create your views here.
def register(request):

    if request.method == "POST":
        data = request.POST
        send_mail(to=data['email'],
                  campaign_json='simulation1/funcs/settings.json',
                  url_id="")
        return render(request, 'landing_page/thanku_page.html')

    return render(request, 'landing_page/lead-page.html')


