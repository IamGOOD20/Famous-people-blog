from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add article/', add_article, name='add_article'),
    path('feedback/', feedback, name='feedback'),
    path('login/', sign_in, name='sign_in'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
