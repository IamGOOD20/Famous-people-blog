from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

class StarsHome(DataMixen, ListView):
      model = Stars
      template_name = 'stars/index.html'
      context_object_name = 'posts'


      def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title='Main page')
            return dict(list(context.items()) + list(c_def.items()))

      def get_queryset(self):
            return Stars.objects.filter(is_published=True).select_related('cat')
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
      #contact_list = Stars.objects.all()
      #paginator = Paginator(contact_list, 3)

      #page_number = request.GET.get('page')
      #page_obj = paginator.get_page(page_number)
      return render(request, 'stars/about.html', {'title': 'About site', 'site_map': site_map}) # 'page_obj': page_obj,


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
class AddPage(LoginRequiredMixin, DataMixen, CreateView):
      form_class = AddPostForm
      template_name = 'stars/addpage.html'
      success_url = reverse_lazy('home')
      login_url = reverse_lazy('home')
      #raise_exception = True # 403

      def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title='Add page')
            return dict(list(context.items()) + list(c_def.items()))


#def feedback(request):
     # return HttpResponse('Feedback')

class FeedbackFormView(DataMixen, FormView):
      form_class = FeedbackForm
      template_name = 'stars/feedback.html'
      success_url = reverse_lazy('home')

      def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title='Feedback')
            return dict(list(context.items()) + list(c_def.items()))

      def form_valid(self, form):
            print(form.cleaned_data)
            return redirect('home')


#def sign_in(request):
      #return HttpResponse('Sign in')

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
class ShowPost(DataMixen, DetailView):
      model = Stars
      template_name = 'stars/post.html'
      slug_url_kwarg = 'post_slug'
      #pk_url_kwarg = post_pk
      context_object_name = 'post'

      def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title=context['post'])
            return dict(list(context.items()) + list(c_def.items()))

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
class StarsCategory(DataMixen, ListView):
      model = Stars
      template_name = 'stars/index.html'
      context_object_name = 'posts'
      allow_empty = False

      def get_queryset(self):
            return Stars.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

      def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c = Category.objects.get(slug=self.kwargs['cat_slug'])
            c_def = self.get_user_context(title='Category - ' + str(c.name), cat_selected=c.pk)
            return dict(list(context.items()) + list(c_def.items()))

def pageNotFound(request, exception):
      return HttpResponseNotFound('<h1>Page not found</h1>')

class RegisterUser(DataMixen, CreateView):
      form_class = RegisterUserForm
      template_name = 'stars/register.html'
      success_url = reverse_lazy('login')

      def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title='Create account')
            return dict(list(context.items()) + list(c_def.items()))

      def form_valid(self, form):
            user = form.save()
            login(self.request, user)
            return redirect('home')

class LoginUser(DataMixen, LoginView):
      form_class = LoginUserForm
      template_name = 'stars/login.html'

      def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title='Authorization')
            return dict(list(context.items()) + list(c_def.items()))

      def get_success_url(self):
            return reverse_lazy('home')


def logout_user(request):
      logout(request)
      return redirect('login')