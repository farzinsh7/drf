from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import TaggedItem
from store.admin import ProductAdmin
from store.models import Product


class TagInlnline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem
    min_num = 1
    max_num = 10
    extra = 0


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInlnline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
