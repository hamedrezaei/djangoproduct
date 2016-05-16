from django.conf.urls import url

from . import views


app_name = 'pycharmfirst'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cat_id>[0-9]+)/$', views.products, name='products'),
    url(r'^categoryaddform/$', views.categoryaddform, name='categoryaddform'),
    url(r'^(?P<cat_id>[0-9]+)/addcategory/$', views.addcategory, name='addcategory')
]