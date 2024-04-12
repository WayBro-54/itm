from django.db import models
from django.contrib.auth import get_user_model

Users = get_user_model()


class Category(models.Model):
    slug = models.SlugField(
        max_length=55,
        unique=True,
        verbose_name='slug of the category',
        help_text='slug of the category'
    )
    name = models.CharField(
        max_length=55,
        unique=True,
        verbose_name='name of the category',
        help_text='name of the category'
    )
    category_watch = models.ManyToManyField(
        'Watch',
        through='CategoryWatch',
        through_fields=('category', 'watch'),
    )

    def __str__(self):
        return f'{self.name} {self.slug}'

    def __repr__(self):
        return f'{type(self).__name__}: {self.name} {self.slug}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Watch(models.Model):
    slug = models.SlugField(
        max_length=55,
        unique=True,
        verbose_name='slug of the watch',
        help_text='slug of the watch',
    )
    name = models.CharField(
        max_length=255,
        verbose_name='name watch',
        help_text='name of the watch',
    )
    description = models.TextField(
        verbose_name='description of the watch',
        help_text='description of the watch',
    )
    price_sell = models.PositiveIntegerField(
        verbose_name='price for customers'
    )
    price_buy = models.PositiveIntegerField(
        verbose_name='purchase price'
    )
    count = models.IntegerField(
        verbose_name='stock balance'
    )

    class Meta:
        verbose_name = 'Watch'
        verbose_name_plural = 'Watches'


class CategoryWatch(models.Model):
    watch = models.ForeignKey(
        'Watch',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'CategoryWatch'
        verbose_name_plural = 'CategoryWatch'


class ShoppingCart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ShoppingCart'
        verbose_name_plural = 'ShoppingCarts'
