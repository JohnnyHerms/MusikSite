from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.note_list, name='note_list'),
]