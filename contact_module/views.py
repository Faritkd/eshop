from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView, CreateView
from .forms import ContactUsModelForm
from .models import ContactUs
from django.views.generic.base import TemplateView


# Create your views here.

class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    model = ContactUs
    form_class = ContactUsModelForm
    success_url = '/contact-us/'




