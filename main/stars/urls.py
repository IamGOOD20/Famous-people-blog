from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', StarsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('feedback/', feedback, name='feedback'),
    path('login/', sign_in, name='sign_in'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', StarsCategory.as_view(), name='category'),
]

