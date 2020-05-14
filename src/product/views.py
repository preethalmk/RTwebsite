from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import (product,
                    productSerial,
                    productImage,
                    offers)

# Create your views here.
class ProductListView(ListView):
    #queryset= Product.objects.all()
    template_name="products/shop.html"

    def get_context_data(self,*args,**kwargs):
        context=super(ProductListView,self).get_context_data(*args,**kwargs)
        print('context :  '+str(context))
        slug = self.kwargs.get("slug")
        print(slug)
        print('args' + str(args))
        print('kwarg' + str(kwargs))
        return context

    def get_object(self,*args,**kwargs):
        print('------------------------')
        request=self.request
        print(request)
        pk=self.kwargs.get("pk")
        instance=Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404(f"{pk} not found")
        return instance

    def get_queryset(self,*args,**kwargs):
        request=self.request
        print('request : '+str(request))
        return product.objects.all()