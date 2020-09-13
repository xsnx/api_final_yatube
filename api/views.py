from rest_framework import viewsets, filters, mixins
import django_filters.rest_framework
from .models import Post, Comment, Follow, Group
from . import serializers
from .permissions import OnlyCreatorPermission


class ViewSet(mixins.CreateModelMixin,
              mixins.ListModelMixin,
              viewsets.GenericViewSet):
    pass


class APIPostDetail(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (OnlyCreatorPermission,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['group']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class APICommentDetail(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = [OnlyCreatorPermission]

    def get_queryset(self):
        self.queryset = Comment.objects.all()
        return self.queryset.filter(post=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class APIGroup(ViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [OnlyCreatorPermission]


class APIFollow(ViewSet):
    serializer_class = serializers.FollowSerializer
    permission_classes = [OnlyCreatorPermission]
    queryset = Follow.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']
