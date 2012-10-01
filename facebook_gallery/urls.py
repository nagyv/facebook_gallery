from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
import models

urlpatterns = patterns('',
    url(r'^$', 
        ListView.as_view(
            queryset=models.Gallery.objects.filter(published=True)), 
        name='list_gallery'),
    url(r'^(?P<pk>\d+)/$', 
        DetailView.as_view(
            model=models.Gallery),
        name='show_gallery'),
)