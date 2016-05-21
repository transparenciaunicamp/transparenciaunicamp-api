from rest_framework import serializers
from api.core.models import Institute, Document, Category, Item


class InstituteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institute
        fields = ('title', 'description', 'parent')


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ('title', 'description', 'institute')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'parent')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
