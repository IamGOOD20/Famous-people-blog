from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .forms import *
from .models import *

site_map = [
      {'title': 'About site', 'url_name': 'about'},
      {'title': 'Add page', 'url_name': 'add_page'},
      {'title': 'Feedback', 'url_name': 'feedback'},
      {'title': 'Sign in', 'url_name': 'sign_in'}
      ]

def index(request):
      posts = Stars.objects.all()

      context = {
            'posts': posts,
            'site_map': site_map,
            'title': 'Main page',
            'cat_selected': 0,
            }

      return render(request, 'stars/index.html', context=context)

def about(request):
      return render(request, 'stars/about.html', {'title': 'About site'})

def add_page(request):
      if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                  #print(form.cleaned_data)
                  try:
                        Stars.objects.create(**form.cleaned_data)
                        return redirect('home')
                  except:
                        form.add_error(None, 'Page not published')
      else:
            form = AddPostForm()
      return render(request, 'stars/addpage.html', {'form': form, "site map": site_map, 'title': 'Add page'})

def feedback(request):
      return HttpResponse('Feedback')

def sign_in(request):
      return HttpResponse('Sign in')

def show_post(request, post_slug):
      post = get_object_or_404(Stars, slug=post_slug)

      context = {
            'post': post,
            'site_map': site_map,
            'title': post.title,
            'cat_selected': post.cat_id,
            }
      return render(request, 'stars/post.html', context=context)

def show_category(request, cat_slug):
      cat = Category.objects.filter(slug=cat_slug)
      posts = Stars.objects.filter(cat_id=cat[0].id)

      context = {
            'posts': posts,
            'site_map': site_map,
            'title': 'By category',
            'cat_selected': cat[0].id,
            }

      if len(posts) == 0:
            raise Http404

      return render(request, 'stars/index.html', context=context)


def pageNotFound(request, exception):
      return HttpResponseNotFound('<h1>Page not found</h1>')