from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import django_filters.rest_framework
from .models import Post, Comment, Follow, Group, User
from api.serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
from api.permissions import OnlyCreatorPermission


class APIPostDetail(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OnlyCreatorPermission,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['group']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class APICommentDetail(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [OnlyCreatorPermission]

    def get_queryset(self):
        self.queryset = Comment.objects.all()
        return self.queryset.filter(post=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class APIGroup(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [OnlyCreatorPermission]
    search_fields = ['title', ]


class APIFollow(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [OnlyCreatorPermission]
    queryset = Follow.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['user', 'following']
    search_fields = ['user', 'following'] #['=user__username', '=following__username']


    # def get_queryset(self):
    #     self.queryset = Follow.objects.all()
    #     following = self.request.query_params.get('user', None)
    #     if following is None:
    #         self.queryset.filter(following=following)

    # def perform_create(self, serializer):
    #     username = self.request.query_params.get('user', None)
    #     if username is None:
    #         user = self.request.user
    #     else:
    #         return Response(status=status.HTTP_403_FORBIDDEN)
    #     serializer.save(user=user)
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    #     serializer.save(following=self.request.user)



