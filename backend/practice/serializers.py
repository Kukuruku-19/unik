from rest_framework import serializers

from .models import GalleryPhoto, Gallery, News, NewsContent


class GalleryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryPhoto
        fields = ['photo']


class GalleryPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'name', 'photo_preview']


class GallerySerializer(serializers.ModelSerializer):
    photo = GalleryPhotoSerializer(many=True, required=False)

    class Meta:
        model = Gallery
        fields = ['id', 'name', 'photo']


class NewsPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', "created_at", 'preview', 'photo_preview']


class NewsContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsContent
        fields = ['text', 'photo']


class NewsSerializer(serializers.ModelSerializer):
    content = NewsContentSerializer(many=True, required=False)

    class Meta:
        model = News
        fields = ['title', "created_at", 'content']
