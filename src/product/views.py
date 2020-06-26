from django.shortcuts import render,redirect
from django.db.models import Max, Min
from django.views.generic import ListView,DetailView
from index.views import get_index_parms
from .models import (product,
                    subCatageory,
                    catageory,
                    productSerial,
                    productImage,
                    offers,
                    brand,
                    size,
                    color)

def filter_data(dic):
    dic['catageoryQs'] =catageory.objects.all()
    dic['MaxPrice'] =max(product.objects.all().aggregate(Max('ProductRate'))['ProductRate__max'],10000)
    dic['MinPrice'] =max(product.objects.all().aggregate(Min('ProductRate'))['ProductRate__min'],1)
    dic['brand'] =brand.objects.all()
    dic['color'] =color.objects.all()
    dic['size'] =size.objects.all()
    return dic


# Create your views here.
class ProductListView(ListView):
    #queryset= Product.objects.all()
    template_name="products/shop.html"

    def get_context_data(self,*args,**kwargs):
        context=super(ProductListView,self).get_context_data(*args,**kwargs)
        print('context :  '+str(context))
        slug = self.kwargs.get("slug")
        #print('slug:'+slug)
        print('args' + str(args))
        print('kwarg' + str(kwargs))
        return get_index_parms(context)

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
        print('person_id : {}'.format(self.kwargs.get("person_id")))
        print('group_id : {}'.format(self.kwargs.get("group_id")))
        print('request : '+str(request))
        return product.objects.all()

class ProductDetails(ListView):

    def __init__(self):
        self.prod_id=17
        self.productQs=product.objects.get_by_id(self.prod_id)

    template_name="products/detail.html"

    def get_context_data(self,*args,**kwargs):
        context=super(ProductDetails,self).get_context_data(*args,**kwargs)
        self.prod_id=self.kwargs.get("prod_id")
        self.prod_id=17
        context['serial']=productSerial.objects.filter(product=self.prod_id).all()
        context['image']=productImage.objects.filter(product=self.prod_id).all()
        context['subcat']=self.productQs.first().subCatageoryId.name
        context['cat']=self.productQs.first().subCatageoryId.catageoryId.name
        context['related']=product.objects.filter(subCatageoryId=self.productQs.first().subCatageoryId).all()[:10]
        print('context :  '+str(get_index_parms(context)))
        return (context)

    def get_queryset(self,*args,**kwargs):
        return self.productQs

class GetProducts(ListView):

    template_name="products/shop.html"

    def get_context_data(self,*args,**kwargs):
        context=super(GetProducts,self).get_context_data(*args,**kwargs)
        self.mode=self.kwargs.get("mode")
        self.filter=self.kwargs.get("filter")
        print('dsadadsasdasd')
        print('context1 :  '+str(filter_data(get_index_parms(context))))
        return filter_data(get_index_parms(context))

    def get_queryset(self,*args,**kwargs):
        request=self.request
        mode=self.kwargs.get("mode")
        print('mode :  '+str(mode))
        filter=self.kwargs.get("filter")
        print('filter :  '+str(filter))

        if mode=="subcat":
            return subCatageory.objects.get_by_id(int(filter)).first().product.all()
        elif mode=="cat":
            return product.objects.filter(subCatageoryId__catageoryId_id=int(filter)).all()
        elif mode=="filter":
            return product.objects.all()
        else:
            return product.objects.all()
