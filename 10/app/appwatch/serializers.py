from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Category, Watch, ShoppingCart

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

    class Meta:
        model = Watch
        fields = (
            'id',
            'name',
            'description',
            'price_sell',
            'price_buy',
            'count',
        )


class ShoppingCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = (
            '',
            '',
        )
