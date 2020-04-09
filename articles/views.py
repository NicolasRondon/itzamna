from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from articles.models import Article, Comment
from articles.serializers import ArticleSerializer, CreateArticleSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrReadOnly]

        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateArticleSerializer
        return ArticleSerializer

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        article = self.get_object()
        comments = Comment.objects.filter(article=article.id)
        serialized = CommentSerializer(comments, many=True)
        if not comments:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'El artículo no tiene comentarios'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)
