from .models import *
from asgiref.sync import sync_to_async


@sync_to_async
def get_article_by_genre(genre):
    return Article.objects.filter(genre=genre).select_related('language').prefetch_related('genre')


@sync_to_async
def get_author_by_name(name):
    return Author.objects.filter(name=name)


@sync_to_async
def get_language_by_name(name):
    return Language.objects.filter(name=name)