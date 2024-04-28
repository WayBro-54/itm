from django.contrib import admin
from .models import (
    Category,
    CategoryWatch,
    Watch,
    ShoppingCart
)


class CategoryWatchTable(admin.TabularInline):
    model = Category.category_watch.through


class ShoppingCartInline(admin.TabularInline):
    model = Watch


@admin.register(CategoryWatch)
class AdminCategoryWatch(admin.ModelAdmin):
    list_display = (
        'watch',
        'category',
    )
    fields = (
        'watch',
        'category',
    )


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    fields = ('slug', 'name')
    list_display = ('slug', 'name')
    inlines = (
        CategoryWatchTable,
    )


@admin.register(Watch)
class AdminWatch(admin.ModelAdmin):
    fields = (
        'slug',
        'name',
        'description',
        'price_sell',
        'price_buy',
        'count',
    )
    list_display = (
        'slug',
        'name',
        'description',
        'price_sell',
        'price_buy',
        'count',
    )
    inlines = (
        CategoryWatchTable,
    )


@admin.register(ShoppingCart)
class AdminShoppingCart(admin.ModelAdmin):
    list_display = ('watch', 'user')
    search_fields = ('watch__name', 'user__email')
    # raw_id_fields = ('user', 'watch')

    def get_queryset(self, request):
        # Переопределяем queryset для оптимизации запросов к базе данных
        return super().get_queryset(request).select_related('user', 'watch')