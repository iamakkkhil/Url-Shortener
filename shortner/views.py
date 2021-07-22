from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.template import Context
import uuid
from .models import url

# Create your views here.
def index(request):
    if request.method == "POST":
        link = request.POST.get('url')
        uid = str(uuid.uuid4())[:5]

        data = url(url=link, uuid=uid)
        data.save()

        host = request.build_absolute_uri('')
        context = {"urlShort" : f'{host}{uid}'}
        return render(request, 'index.html', context)
        
    return render(request, 'index.html')


def go(request, uid):
    link = url.objects.filter(uuid=uid).first()
    if link:
        return HttpResponseRedirect(link.url)
    else:
        return render(request, 'invalid.html')