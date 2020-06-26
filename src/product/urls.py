from django.urls import path,re_path

from .views import (
        ProductListView,
        GetProducts,
        ProductDetails,
        )
app_name = 'product'
urlpatterns = [
    path('', ProductListView.as_view(),name='shop'),
    path('<str:mode>/<str:filter>',GetProducts.as_view(),name='listprod'),
    path('<int:prod_id>',ProductDetails.as_view(),name='details')
]
