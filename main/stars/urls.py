from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('news/<int:newsid>/', news),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive),
]
