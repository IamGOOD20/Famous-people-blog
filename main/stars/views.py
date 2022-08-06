from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

site_map = [
      {'title': 'About site', 'url_name': 'about'},
      {'title': 'Add article', 'url_name': 'add_article'},
      {'title': 'Feedback', 'url_name': 'feedback'},
      {'title': 'Sign in', 'url_name': 'sign_in'}
      ]

def index(request):
      posts = Stars.objects.all()
      cats = Category.objects.all()

      context = {
            'posts': posts,
            'cats': cats,
            'site_map': site_map,
            'title': 'Main page',
            'cat_selected': 0,
            }

      return render(request, 'stars/index.html', context=context)

def about(request):
      return render(request, 'stars/about.html', {'title': 'About site'})

def add_article(request):
      return HttpResponse('Add article')

def feedback(request):
      return HttpResponse('Feedback')

def sign_in(request):
      return HttpResponse('Sign in')

def show_post(request, post_id):
      return HttpResponse(f'Article display with id = {post_id}')

def show_category(request, cat_id):
      posts = Stars.objects.filter(cat_id=cat_id)
      cats = Category.objects.all()

      context = {
            'posts': posts,
            'cats': cats,
            'site_map': site_map,
            'title': 'By category',
            'cat_selected': cat_id,
            }

      if len(posts) == 0:
            raise Http404

      return render(request, 'stars/index.html', context=context)


def pageNotFound(request, exception):
      return HttpResponseNotFound('<h1>Page not found</h1>')