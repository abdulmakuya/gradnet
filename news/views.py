from django.shortcuts import render


#these imports support the good ol way of loader and templates seen in def newname2 rendering events
from django.http import HttpResponse
from django.template import loader

from event.models import event

# Create your views here.
def newsview(request):
        all_news = news.objects.all()
        template = loader.get_template('newspage/eventmanifest - new.html')
        context = { 'all_news' : all_news, }
        return HttpResponse(template.render(context, request))