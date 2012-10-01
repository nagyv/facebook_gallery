from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from facebook_gallery import facebook_api

class Command(BaseCommand):
    args = '<page_id page_id ...>'
    help = "Fetches the albums related to an facebook id. Should be called with one or more facebook object ids"

    def handle(self, *page_ids, **kwargs):
        for page_id in page_ids:
            self.stdout.write('Fetching albums for page %s' % page_id)
            try:
                albums = facebook_api.fetch_albums(int(page_id))
            except Exception, e:
                raise
                self.stderr.write('Fetching failed', e)
            else:
                self.stdout.write('Albums fetched')
        

