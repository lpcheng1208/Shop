from .models import Goods, GoodsImage, GoodsCategory, Banner, HotSearchWords, Video
from .serializers import GoodsSerializer, GoodsImageSerializer, CategorySerializer, \
    BannersSerializer, HotSearchWordsSerializer, VideoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
from rest_framework import filters


class GoodsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:

    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class ImageListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsImage.objects.filter(goods_id=1)
    serializer_class = GoodsImageSerializer


class BannersListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannersSerializer


class HotSearchWordsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = HotSearchWords.objects.all()
    serializer_class = HotSearchWordsSerializer


class VideoListViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by("id")
    serializer_class = VideoSerializer
    pagination_class = GoodsPagination
