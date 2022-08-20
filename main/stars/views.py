from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from .forms import *
from .models import *



site_map = [
      {'title': 'About site', 'url_name': 'about'},
      {'title': 'Add page', 'url_name': 'add_page'},
      {'title': 'Feedback', 'url_name': 'feedback'},
      {'title': 'Sign in', 'url_name': 'sign_in'}
      ]

class StarsHome(ListView):
      model = Stars
      template_name = 'stars/index.html'
      context_object_name = 'posts'


      def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['site_map'] = site_map
            context['title'] = 'Main page'
            context['cat_selected'] = 0
            return context

      def get_queryset(self):
            return Stars.objects.filter(is_published=True)
'''
def index(request):
      posts = Stars.objects.all()

      context = {
            'posts': posts,
            'site_map': site_map,
            'title': 'Main page',
            'cat_selected': 0,
            }

      return render(request, 'stars/index.html', context=context)
'''


def about(request):
      return render(request, 'stars/about.html', {'title': 'About site'})


'''
def add_page(request):
      if request.method == 'POST':
            form = AddPostForm(request.POST, request.FILES)
            if form.is_valid():
                  #print(form.cleaned_data
                  form.save()
                  return redirect('home')
      else:
            form = AddPostForm()

      return render(request, 'stars/addpage.html', {'form': form, "site map": site_map, 'title': 'Add page'})
'''
class AddPage(CreateView):
      form_class = AddPostForm
      template_name = 'stars/addpage.html'
      success_url = reverse_lazy('home')

      def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['site_map'] = site_map
            context['title'] = 'Add page'
            return context


def feedback(request):
      return HttpResponse('Feedback')

def sign_in(request):
      return HttpResponse('Sign in')

'''
def show_post(request, post_slug):
      post = get_object_or_404(Stars, slug=post_slug)

      context = {
            'post': post,
            'site_map': site_map,
            'title': post.title,
            'cat_selected': post.cat_id,
            }
      return render(request, 'stars/post.html', context=context)
'''
class ShowPost( DetailView):
      model = Stars
      template_name = 'stars/post.html'
      slug_url_kwarg = 'post_slug'
      #pk_url_kwarg = post_pk
      context_object_name = 'post'

      def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['site_map'] = site_map
            context['title'] = context['post']
            context['cat_selected'] = 0
            return context

'''
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
'''
class StarsCategory(ListView):
      model = Stars
      template_name = 'stars/index.html'
      context_object_name = 'posts'
      allow_empty = False

      def get_queryset(self):
            return Stars.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

      def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['site_map'] = site_map
            context['title'] = 'Category - ' + str(context['posts'][0].cat)
            context['cat_selected'] = context['posts'][0].cat_id
            return context

def pageNotFound(request, exception):
      return HttpResponseNotFound('<h1>Page not found</h1>')