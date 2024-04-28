# Generated by Django 4.2 on 2024-04-22 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appwatch', '0004_alter_category_category_watch'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='watch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='appwatch.watch'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category_watch',
            field=models.ManyToManyField(through='appwatch.CategoryWatch', to='appwatch.watch'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]