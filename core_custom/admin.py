from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import User
from tags.models import TaggedItem
from store.admin import ProductAdmin
from store.models import Product


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "first_name", "last_name", "password1", "password2", "email"),
            },
        ),
    )


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
