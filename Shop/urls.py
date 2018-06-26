"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from Shop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from users.views import SmsCodeViewSet, UserViewSet
from goods.views import GoodsListViewSet, CategoryViewSet, ImageListViewSet, BannersListViewSet, \
    HotSearchWordsListViewSet
from user_operation.views import UserFavViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')
router.register(r'codes', SmsCodeViewSet, base_name='codes')
router.register(r'categorys', CategoryViewSet, base_name='categorys')
router.register(r'banners', BannersListViewSet, base_name='banners')
router.register(r'hotsearchs', HotSearchWordsListViewSet, base_name='hotsearchs')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'userfavs', UserFavViewSet, base_name='userfavs')

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^', include(router.urls)),
    # 商品列表
    url(r'docs/', include_docs_urls(title="生鲜超市")),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^login/', obtain_jwt_token),
]
