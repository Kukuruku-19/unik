from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import GalleryAPIView, NewsAPIView, GalleryRetrieve, NewsRetrieve

urlpatterns = [
    path('gallery/', GalleryAPIView.as_view()),
    path('gallery/<int:pk>', GalleryRetrieve.as_view()),
    path('news/', NewsAPIView.as_view()),
    path('news/<int:pk>', NewsRetrieve.as_view()),
]
