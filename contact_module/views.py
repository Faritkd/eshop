from django.views.generic import ListView
from django.views.generic import CreateView
from .forms import ContactUsModelForm
from .models import ContactUs, UserProfile


# Create your views here.

class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    model = ContactUs
    form_class = ContactUsModelForm
    success_url = '/contact-us/'


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'


class ProfilesView(ListView):
    template_name = 'contact_module/profile_list_page.html'
    model = UserProfile
    context_object_name = 'profiles'


