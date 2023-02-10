from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Gallery, News, GalleryPhoto, NewsContent

# Register your models here.
admin.site.unregister(Group)
admin.site.register(Gallery)
admin.site.register(GalleryPhoto)
admin.site.register(News)
admin.site.register(NewsContent)

