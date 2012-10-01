from django.db import models
from django.utils.translation import ugettext as _

class Gallery(models.Model):
    id = models.BigIntegerField(editable=False, primary_key=True)
    name = models.CharField(max_length=255, editable=False)
    description = models.TextField(blank=True, editable=False)
    cover_photo = models.TextField(editable=False, default='')
    count = models.IntegerField(editable=False)
    album_type = models.CharField(max_length=255, choices=[('profile', 'Profile'),
        ('mobile', 'Mobile'),
        ('wall', 'Wall'),
        ('normal', 'Normal'),
        ('album', 'Album'),], editable=False)
    created_time = models.DateTimeField(editable=False)
    updated_time = models.DateTimeField(editable=False)
    published = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')
        ordering = ["created_time", "updated_time", "name"]

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('show_gallery', (), {'pk': str(self.id)})

    def publish(self):
        self.published = True
        self.save()
        return self

    def unpublish(self):
        self.published = False
        self.save()
        return self

    def get_cover_photo(self):
        if self.cover_photo:
            return self.cover_photo
        elif self.image_set.count() > 0:
            return self.image_set.all()[0].thumbnail
        else:
            return None

class Image(models.Model):
    id = models.BigIntegerField(editable=False, primary_key=True)
    gallery = models.ForeignKey(Gallery, editable=False)
    thumbnail = models.TextField(editable=False)
    image = models.TextField(editable=False)
