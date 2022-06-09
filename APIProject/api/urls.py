from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

from django.views.generic import RedirectView

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
#router.register('', ArticleViewSet, basename='articles')
router.register('author', AuthorViewSet, basename='author')
router.register('genre', GenreViewSet, basename='genre')

urlpatterns = [
    path('', include(router.urls)),
    path('articless', ArticleViewSet.as_view({'get':'list'}), name='articless'),
]
