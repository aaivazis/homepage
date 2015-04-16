# sitemaps.py
from django.contrib import sitemaps
from django.core.urlresolvers import reverse

class Sitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['about', 'projects']

    def location(self, item):
        return reverse(item)