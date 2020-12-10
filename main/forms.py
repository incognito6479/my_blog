from django.forms import ModelForm
from django import forms
from .models import MakePost
from django.utils.translation import gettext_lazy as _


class SignupForm(forms.Form):
    name = forms.CharField(max_length=50, label=_('Name'))
    email = forms.EmailField()
    login = forms.CharField(max_length=50, label=_('Login'))
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))


class LoginForm(forms.Form):
    login = forms.CharField(max_length=30, label=_('Login'))
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))


class PostForms(ModelForm):
    class Meta:
        model = MakePost
        fields = ['post_title', 'post_text', 'post_img']
        labels = {
            'post_title': _('Title for your post'),
            'post_text': _('Text for your post'),
            'post_img': _('Select image for your post')
        }
