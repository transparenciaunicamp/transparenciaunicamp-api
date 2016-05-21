from rest_framework import viewsets
from api.core.models import Institute, Document, Category, Item
from api.core.serializers import (InstituteSerializer, DocumentSerializer,
                                  CategorySerializer, ItemSerializer)


# ViewSets define the view behavior.
class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
