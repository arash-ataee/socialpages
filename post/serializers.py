from rest_framework import serializers

from .models import Post, Subcategory, Category, MediaFile, Rate
from page.serializers import PageSerializer
from user.serializers import ProfileSerializer


class SubcategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Subcategory
        fields = ['url', 'id', 'name', 'num_chasers']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'num_chasers', 'subcategories']


class SubcategoryDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    chasers = ProfileSerializer(many=True)

    class Meta:
        model = Subcategory
        fields = ['name', 'id', 'category', 'chasers', 'num_chasers']


class CategoryDetailSerializer(serializers.ModelSerializer):
    chasers = ProfileSerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'id', 'chasers', 'num_chasers']


class HideMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaFile
        fields = ['id', 'price', 'file_size']


class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaFile
        fields = ['id', 'file_size', 'file']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    sender = ProfileSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['url', 'id', 'sender', 'title', 'cover']


class PostDetailSerializer(serializers.ModelSerializer):
    store = PageSerializer()
    sender = ProfileSerializer(read_only=True)
    subcategories = SubcategorySerializer(many=True)
    viewed_by = ProfileSerializer(many=True)
    views = serializers.SerializerMethodField()

    def get_views(self, Post):
        return Post.viewed_by.all().count()

    class Meta:
        model = Post
        fields = [
            'id',
            'page',
            'sender',
            'title',
            'caption',
            'subcategories',
            'viewed_by',
            'views',
            'is_special',
            'price',
        ]


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ['rate']