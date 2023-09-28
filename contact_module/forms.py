from django import forms


class ContactUsForm(forms.Form):
    title = forms.CharField()
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

