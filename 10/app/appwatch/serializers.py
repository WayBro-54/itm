from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Category, Watch, ShoppingCart, CategoryWatch

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'slug',
            'name',
        )


class WatchSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Watch
        fields = (
            'id',
            'name',
            'categories',
            'description',
            'price_sell',
            'price_buy',
            'count',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        categories = CategoryWatch.objects.filter(watch=instance).values_list('category__slug', 'category__name')
        representation['categories'] = [{'slug': slug, 'name': name} for slug, name in categories]
        return representation


class ShoppingCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = (
            'watch',
        )
