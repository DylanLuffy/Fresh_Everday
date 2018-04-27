from django.conf.urls import url
from apps.cart.views import CartView,CartInfoview,CartUpdateView,CartDeleteView


urlpatterns = [
    url(r'^add$',CartView.as_view(),name='add'),# 购物车记录添加
    url(r'^$',CartInfoview.as_view(),name='show'),# 购物车页面显示
    url(r'^update',CartUpdateView.as_view(),name='update'),# 购物车更新
    url(r'^delete$',CartDeleteView.as_view(),name = 'delete'),# 删除购物车记录
]
