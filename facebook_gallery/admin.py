from operator import attrgetter

from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib import messages
from django.template import RequestContext

import models
import facebook_api

def fetch_albums(request, *args, **kwargs):
    if request.method == 'POST':
        if request.POST.get('page_id', False):
            albums = facebook_api.fetch_albums(int(request.POST['page_id']))
            if albums:
                messages.add_message(request, messages.SUCCESS, "The albums were fetched")
            else:
                messages.add_message(request, messages.ERROR, "There was an error fetching the albums. Please, try again later.")
        else:
            messages.add_message(request, messages.ERROR, "Please provide an object ID")
        return redirect(reverse('admin:index'))
    else:
        return render_to_response('facebook_gallery/fetch_album_form.html', context_instance=RequestContext(request))
admin.site.register_view('fetch_albums', fetch_albums)

def delete_images(modeladmin, request, queryset):
    """Deleted the images of the selected galleries"""
    del_method = attrgetter('delete')
    for gallery in queryset:
        map(del_method, gallery.image_set.all())
        gallery.count = 0
        gallery.save()
        modeladmin.message_user(request, "The images were deleted")
    return redirect(reverse('admin:index'))
delete_images.short_description = "Delete related images"

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'published']
    list_filter = ['published']
    ordering = ['created_time']
    actions = ['fetch_images', 'publish', 'unpublish', delete_images]

    def fetch_images(self, request, queryset):
        for album in queryset:
            facebook_api.fetch_album(album)
        self.message_user(request, "Images fetched for albums: %s" % ', '.join(map(lambda q: q.name, queryset)))
    fetch_images.short_description = "Fetch images"

    def publish(self, request, queryset):
        for album in queryset:
            album.publish()
    publish.short_description = 'Publish'

    def unpublish(self, request, queryset):
        for album in queryset:
            album.unpublish()
    unpublish.short_description = 'Unpublish'

admin.site.register(models.Gallery, GalleryAdmin)