from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'fb', views.index, name='index'),
]