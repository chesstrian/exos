from django.conf.urls import url
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from app import views

urlpatterns = [
    url(r'^$', view=views.home, name='home'),
    url(r'users/list/$', view=ListView.as_view(model=User), name='user_list'),
    url(r'users/add/$', view=views.UserCreate.as_view(), name='user_add'),
    url(r'users/view/$', view=views.user_select, name='user_view'),
    url(r'users/view/(?P<pk>\d+)/$', view=DetailView.as_view(model=User), name='user_view_item'),
    url(r'users/edit/$', view=views.user_select, name='user_edit'),
    url(r'users/edit/(?P<pk>\d+)/$', view=views.user_edit, name='user_edit_item'),
    url(r'users/delete/$', view=views.user_select, name='user_delete'),
    url(r'users/delete/(?P<pk>\d+)/$', view=views.UserDelete.as_view(), name='user_delete_item'),
    url(r'export/xls/$', views.export_xls, name='export_xls'),
]
