from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add page/', add_page, name='add_page'),
    path('feedback/', feedback, name='feedback'),
    path('login/', sign_in, name='sign_in'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
]
