from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.forms import ModelForm

# from django.core.mail import send_main => メールの送信
# BadHeaderErrorは内容を改ざんするセキュリティ攻撃を検出した際に生成される

class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)
    sender = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)

