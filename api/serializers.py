from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile, Post, Comment

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        # クライアント側から読み込まれないようにする処理
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):

    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'nickName', 'userProfile', 'created_on', 'img')
        # クライアント側から読み込まれないようにする処理
        extra_kwargs = {'userProfile': {'read_only': True}}

class PostSerializer(serializers.ModelSerializer):

    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'userPost', 'created_on', 'img', 'liked')
        # クライアント側から読み込まれないようにする処理
        extra_kwargs = {'userPost': {'read_only': True}}

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'text', 'userComment', 'post')
        # クライアント側から読み込まれないようにする処理
        extra_kwargs = {'userComment': {'read_only': True}}