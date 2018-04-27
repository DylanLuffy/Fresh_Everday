from django.conf.urls import url
from apps.order import views
from apps.order.views import OrderPlaceView,OrderCommitView

urlpatterns = [
    url(r'^place$',OrderPlaceView.as_view(),name='place'), # 提交订单
    url(r'^commit$', OrderCommitView.as_view(), name='commit'), # 订单创建
]
