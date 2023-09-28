from django.shortcuts import render, redirect
from .forms import ContactUsForm, ContactUsModelForm
from .models import ContactUs


# Create your views here.


def contact_us_page(request):
    if request.method == 'POST':
        contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('home_page')
    else:
        contact_form = ContactUsModelForm()

    return render(request, 'contact_module/contact_us_page.html',
                  {'contact_form': contact_form})
