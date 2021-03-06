from django.conf.urls import url

from . import views

app_name = 'showcase'

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='product_detail'),
]
