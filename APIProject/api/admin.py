from django.contrib import admin
from .models import Author, Genre, Article,Language


admin.site.register(Genre)
admin.site.register(Language)
# Register your models here.


class ArticleInline(admin.TabularInline):
    model = Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [ArticleInline]