from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Watch, ShoppingCart
from .serializers import CategorySerializer, WatchSerializer, ShoppingCartSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'name',
        'slug',
    )


class WatchGetList(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer


class ShoppingView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)