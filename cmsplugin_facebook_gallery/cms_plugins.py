from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models import CMSPlugin

from facebook_gallery import models

from django.utils.translation import ugettext as _

class GalleryPlugin(CMSPluginBase):
    model = CMSPlugin # Model where data about this plugin is saved
    name = _("Gallery list") # Name of the plugin
    render_template = "facebook_gallery/gallery_menu.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'object_list':models.Gallery.objects.filter(published=True)})
        return context

plugin_pool.register_plugin(GalleryPlugin) # register the plugin
