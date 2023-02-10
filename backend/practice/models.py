from django.db import models


# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length=50)
    photo_preview = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name


class GalleryPhoto(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='photo')


class News(models.Model):
    title = models.CharField(max_length=200)
    preview = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo_preview = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title


class NewsContent(models.Model):
    text = models.TextField(blank=True, default="Lorem ipsum dolor sit amet")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='content')

