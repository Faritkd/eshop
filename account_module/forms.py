from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[validators.MaxLengthValidator(100), validators.EmailValidator]
    )
    password = forms.CharField(
        label='رمز عبور ',
        widget=forms.PasswordInput(),
    )
    confirm_password = forms.CharField(
        label='تایید رمز عبور ',
        widget=forms.PasswordInput(),
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data['confirm_password']
        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('کلمه عبور و تکرار آن مغایرت دارند')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[validators.MaxLengthValidator(100), validators.EmailValidator]
    )
    password = forms.CharField(
        label='رمز عبور ',
        widget=forms.PasswordInput(),
    )


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[validators.MaxLengthValidator(100), validators.EmailValidator]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='رمز عبور ',
        widget=forms.PasswordInput(),
    )
    confirm_password = forms.CharField(
        label='تایید رمز عبور ',
        widget=forms.PasswordInput(),
    )