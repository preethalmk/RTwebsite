"""index URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,re_path,include
from .views import (index_page,
                    login_page,
                    contact_page,
                    register_page,
                    blog_page,
                    blog_details_page,
                    check_out_page,
                    faq_page,
                    product_page,
                    shop_page,
                    shopping_cart_page
                    )

app_name = 'main_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page,name='index'),
    path('login/', login_page,name='login'),
    path('contact/', contact_page,name='contact'),
    path('register/', register_page,name='register'),
    path('blog/', blog_page,name='blog'),
    path('blogdetails/',blog_details_page,name='blogdetails' ),
    path('checkout/',check_out_page,name='checkout'),
    path('faq/',faq_page,name='faq'),
    path('products/',include("product.urls",namespace="product")),
    #path('product/',product_page,name='product'),
    #path('shop/',shop_page,name='shop'),
    #path('shoppingcart/',shopping_cart_page,name='shoppingcart')

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)