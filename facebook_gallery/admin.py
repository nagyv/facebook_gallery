from django.contrib import admin

import models
import facebook_api

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'published']
    list_filter = ['published']
    ordering = ['created_time']
    actions = ['fetch_images', 'publish', 'unpublish']

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