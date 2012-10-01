import logging
import datetime

from django.conf import settings

import facepy
import models

app_graph = None
def get_app_graph():
    """
    Returns the Graph object for the current app
    """
    global app_graph
    try:
        app_graph.get('%s/app_domains' % settings.FACEBOOK_APP_ID)
    except:
        APP_TOKEN = facepy.get_application_access_token(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
        app_graph = facepy.GraphAPI(APP_TOKEN)
    return app_graph

def fetch_albums(page_id):
    graph = get_app_graph()

    albums = graph.get('%d/albums' % page_id)
    albums = graph.get('', ids=map(lambda album: album['id'], albums['data']), 
        fields='id,name,description,count,type,created_time,updated_time,cover_photo')
    
    for id, album in albums.items():

        try:
            cover_photo = graph.get(album['cover_photo'])
            cover_photo = filter(lambda d: d['width'] <= 180, cover_photo['images'])[0]['source']
        except KeyError:
            cover_photo = ''

        album_data = {
            u'id': int(id),
            u'name': album['name'],
            u'description': album['description'] if album.has_key('description') else '',
            u'cover_photo': cover_photo,
            u'count': album['count'] if album.has_key('count') else 0,
            u'album_type': album['type'],
            u'created_time': datetime.datetime.strptime(album['created_time'], '%Y-%m-%dT%H:%M:%S+0000'),
            u'updated_time': datetime.datetime.strptime(album['updated_time'], '%Y-%m-%dT%H:%M:%S+0000'),
        }
        models.Gallery.objects.get_or_create(id=int(id), defaults=album_data)
    return True

def fetch_album(album):
    images = get_app_graph().get('%d/photos' % album.pk)['data']
    for image in images:
        image_data = {
            'id': image['id'],
            'thumbnail': image['picture'],
            'image': image['source'],
            'gallery': album
        }
        image, created = models.Image.objects.get_or_create(**image_data)
        if created:
            album.image_set.add(image)
    return album
