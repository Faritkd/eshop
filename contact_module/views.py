from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.views.generic import FormView, CreateView
from .forms import ContactUsModelForm, ProfileForm
from .models import ContactUs, UserProfile


# Create your views here.

class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    model = ContactUs
    form_class = ContactUsModelForm
    success_url = '/contact-us/'


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'contact_module/create_profile_page.html',
                      {'form': form})

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return redirect('/contact-us/create-profile')
        return render(request, 'contact_module/create_profile_page.html',
                      {'form': submitted_form})


