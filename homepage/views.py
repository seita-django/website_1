from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from .models import Topic
from .forms import ContactForm
from django.core.mail import EmailMessage

# Template Views with CBV
""""
class IndexView(TemplateView):
    template_name = 'homepage/index.html'
"""
# This time I use def instead...

# main page and response of contact

"""
def index(request):
    return render(request, "homepage/index.html")
"""

"""
def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['itstudent.jp@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('homepage/complete')
    return render(request, "homepage/index.html", {'form': form})
"""
def index(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            email = EmailMessage(
                                   from_email=sender,
                                   subject=subject,
                                   body=message,
                                   to=["itstudent.jp@gmail.com"],
                                   cc=[sender], # If you want to send more than 2 ppl, add their address here
                                   )

            try:
                email.send()
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect('homepage:complete')

    else:
        form = ContactForm()

    return render(request, 'homepage/index.html', {'form': form})

"""
「POST」されたフォームの内容を「form.is_valid()」で検証し正しければ「complete.html」に渡されるという記述。
"""

# Contact completed
def complete(request):
    return render(request, 'homepage/complete.html')

# Q and A
# Post from Admin page for Q and A
def QandA(request):
    queryset = Topic.objects.all()
    context = { "QandA":queryset }
    return render(request, 'homepage/QandA.html', context)

