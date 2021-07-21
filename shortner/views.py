from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.template import Context
import uuid
from .models import url
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == "POST":
        link = request.POST.get('url')
        uid = str(uuid.uuid4())[:5]

        data = url(url=link, uuid=uid)
        data.save()

        context = {"urlShort" : f'{settings.ALLOWED_HOSTS[0]}/{uid}'}
        return render(request, 'index.html', context)
        
    return render(request, 'index.html')


def go(request, uid):
    link = url.objects.filter(uuid=uid).first()
    if link:
        return HttpResponseRedirect(link.url)
    else:
        return HttpResponse("<h3>Invalid URL</h3>")
