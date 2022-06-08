from rest_framework import serializers
from .models import Article, Genre, Author
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class AuthorSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'articles']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', ]


class ArticleSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'genre', 'author', 'language']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']