from django.shortcuts import HttpResponse,render
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.Http_200_OK)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]