from django.conf.urls import url
from .views import post_list

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
]