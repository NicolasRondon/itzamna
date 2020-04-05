from django.shortcuts import render
from  rest_framework import viewsets
# Create your views here.
from articles.models import Article
from articles.serializers import ArticleSerializer, CreateArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateArticleSerializer
        return ArticleSerializer

