from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url('^logout', views.logout, name='logout'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url('^(?P<pk>[0-9]+)/$', views.details, name='details'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url('^(?P<pk>[0-9]+)/update$', views.Updatecategory.as_view(), name="update"),
    url('^(?P<pk>[0-9]+)/delete$', views.Deletecategory.as_view(), name="delete"),
    url(r'^category/(?P<pk>[0-9]+)$', views.mybooks, name='mybooks'),
    url(r'^allbooks', views.allbooks, name='allbooks'),
    url(r'^allcategories', views.allcategories, name='allcategories'),

]