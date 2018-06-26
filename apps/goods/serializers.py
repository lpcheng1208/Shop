from rest_framework import serializers
from .models import Goods, GoodsCategory, GoodsImage, Banner, HotSearchWords


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"


class HotSearchWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
        fields = "__all__"
