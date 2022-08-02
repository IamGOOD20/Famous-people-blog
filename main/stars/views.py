from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

site_map = ['About site', 'Add article', 'Feedback', 'Input']

def index(request):
      posts = Stars.objects.all()
      return render(request, 'stars/index.html', {'posts': posts, 'site_map': site_map,  'title': 'Main page'})

def about(request):
      return render(request, 'stars/about.html', {'title': 'About site'})

def news(request, newsid):
      return HttpResponse(f'<h1>There will be all news!<p>{newsid}</p></h1>')

def archive(request, year):
      if int(year) > 2020:
            return redirect('home', permanent=False)

      return HttpResponse(f'<h1>Archive by years</h1><p>{year}</p>')

def pageNotFound(request, exception):
      return HttpResponseNotFound('<h1>Page not found</h1>')

