from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from articles.models import Article
from articles.serializers import ArticleSerializer, CreateArticleSerializer
from .permissions import IsOwnerOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateArticleSerializer
        return ArticleSerializer

