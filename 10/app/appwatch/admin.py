from django.contrib import admin
from .models import (
    Category,
    CategoryWatch,
    Watch,
    ShoppingCart
)


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(CategoryWatch)
class AdminCategoryWatch(admin.ModelAdmin):
    pass


@admin.register(Watch)
class AdminWatch(admin.ModelAdmin):
    pass


@admin.register(ShoppingCart)
class AdminShoppingCart(admin.ModelAdmin):
    pass
