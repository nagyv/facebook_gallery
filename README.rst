Facebook Gallery app for Django
================================

This is a simple gallery app for django that fetches your Galleries from facebook, and shows them in your site. This way you don't have to bother with storage and thumbnail generation, Facebook does it for you. End it's extremely easy to administer, as you should manage your galleries (almost) only at facebook.

Requirements
--------------

* Django (checked with 1.4+)
* facepy

Installation
-------------

Add `facebook_gallery` to your `INSTALLED_APPS`, and set two settings variables:

    settings.FACEBOOK_APP_ID = ''
    settings.FACEBOOK_APP_SECRET = ''

Usage
------

Run the management command `fetch_albums <object_id>` to fetch the albums owned by the Facebook object <object_id>.
This would fetch the basic gallery data from facebook. Afterwards, you can publish and fetch the images for a given gallery from the django admin interface.

Customization
--------------

The galleries are shown using two templates:

* gallery_list.html
* gallery_detail.html

Extras
------

The included `cmsplugin_facebook_gallery` adds easy integration to `django-cms` as an app. Simply install it by adding `cmsplugin_facebook_gallery` to `INSTALLED_APPS`. You will find a new "Gallery" option under your Application list in your pages' edit view.

Running the Tests
------------------------------------

You can run the tests with via::

    python setup.py test

or::

    python runtests.py


Websites using this app
------------------------

* [Jalagati Jóga Egyesület](http://jalagat.hu)