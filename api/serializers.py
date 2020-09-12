from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
     )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
     )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    # following = serializers.CharField(source='following.username')
    # user = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='user'
    # )
    # following = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='following'
    # )
    #user = serializers.ReadOnlyField(source='user.username')
    user = serializers.SlugRelatedField(many=False, read_only=True, slug_field="username")
    following = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(),
        slug_field='username',
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
