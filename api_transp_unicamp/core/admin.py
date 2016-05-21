from django.contrib import admin
from api_transp_unicamp.core.models import Category, Item


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')


class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'value')


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Item, ItemModelAdmin)
