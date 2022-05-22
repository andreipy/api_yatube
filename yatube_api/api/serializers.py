from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    group = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Group.objects.all(),
        required=False
    )

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        read_only_fields = ('author',)
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post',)
        model = Comment
