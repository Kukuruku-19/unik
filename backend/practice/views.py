from django.shortcuts import render

# Create your views here.


from rest_framework import generics

from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Gallery, GalleryPhoto, News, NewsContent
from .serializers import GallerySerializer, NewsSerializer, NewsPreviewSerializer, GalleryPreviewSerializer


class GalleryAPIView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryPreviewSerializer


class GalleryRetrieve(generics.RetrieveAPIView):
    queryset = Gallery.objects.prefetch_related('photo')
    serializer_class = GallerySerializer


class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsPreviewSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title',)
    ordering_fields = ("created_at",)



class NewsRetrieve(generics.RetrieveAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.prefetch_related('content').all()

