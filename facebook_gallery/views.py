from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

import models

class GalleriesListView(ListView):
    queryset = models.Gallery.objects.filter(published=True)

class GalleryView(DetailView):
    queryset = models.Gallery.objects.filter(published=True)
