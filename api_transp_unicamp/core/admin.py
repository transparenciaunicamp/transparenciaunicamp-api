from django.contrib import admin
from api_transp_unicamp.core.models import (
    Institute, Document, Category, Item
)


class InstituteModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')


class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'institute', 'category', 'month', 'year')


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')


class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'value')


admin.site.register(Institute, InstituteModelAdmin)
admin.site.register(Document, DocumentModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Item, ItemModelAdmin)
