from rest_framework import viewsets
from api.core.models import Institute, Document, Category, Item
from api.core.serializers import (InstituteSerializer, DocumentSerializer,
                                  CategorySerializer, ItemSerializer)


# ViewSets define the view behavior.
class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer

    def get_queryset(self):
        queryset = Institute.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_queryset(self):
        queryset = Document.objects.all()
        title = self.request.query_params.get('title', None)
        institute = self.request.query_params.get('institute', None)
        category = self.request.query_params.get('category', None)
        month = self.request.query_params.get('month', None)
        year = self.request.query_params.get('year', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        if institute is not None:
            queryset = queryset.filter(institute=institute)
        if category is not None:
            queryset = queryset.filter(category=category)
        if month is not None:
            queryset = queryset.filter(month=month)
        if year is not None:
            queryset = queryset.filter(year=year)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Institute.objects.all()
        title = self.request.query_params.get('title', None)
        category = self.request.query_params.get('category', None)
        value = self.request.query_params.get('value', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        if category is not None:
            queryset = queryset.filter(category=category)
        if value is not None:
            queryset = queryset.filter(value=value)
        return queryset
