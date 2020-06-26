from django.shortcuts import render,redirect
from customModels.models import common,commonTypes
from product.models import (catageory,
                            subCatageory,
                            product,
                            productSerial,
                            productImage,
                            offers)

def get_index_parms(context_dic):
    #get common Types Id
    context_dic['dealOfTheDayQS']      = commonTypes.objects.filter(typeName='DealOfTheDay').first().common.first()
    context_dic['PartnerLogoQS']       = commonTypes.objects.filter(typeName='PartnerLogo').first().common.all()
    context_dic['footerLogoQS']        = commonTypes.objects.filter(typeName='FooterLogo').first().common.first()
    context_dic['headerLogoQS']        = commonTypes.objects.filter(typeName='HeaderLogo').first().common.first()
    context_dic['heroLogoQS']           = commonTypes.objects.filter(typeName='Hero').first().common.all()
    context_dic['addressQS']           = commonTypes.objects.filter(typeName='Address').first().common.first()
    context_dic['phoneQS']             = commonTypes.objects.filter(typeName='Phone').first().common.first()
    context_dic['emailQS']             = commonTypes.objects.filter(typeName='Email').first().common.first()
    context_dic['paymentMethodLogoQS'] = commonTypes.objects.filter(typeName='PaymentMethod').first().common.first()
    return context_dic

def index_page(request):
	catageoryQuerySet={}
	for c in catageory.objects.all():
		subcat={}
		for sc in c.subcatageory.all():
			subcat[sc]=sc.product.all()
		catageoryQuerySet[c]=subcat

	#MainlogUrl=common.objects.filter(Name='headerLogo',typeName=logoid).first().image.url
	context={
		"title" :"RT Home",
		"catageoryQuerySet":catageoryQuerySet
	}
	return render(request,"index.html",get_index_parms(context))

def login_page(request):
	context={
	"title" :"RT Login"
	}
	#print(request.user.is_authenticated)
	return render(request,"login.html",get_index_parms(context))

def contact_page(request):
	context={
	"title" :"RT Contact"
	}
	#print(request.user.is_authenticated)
	return render(request,"contact.html",get_index_parms(context))

def register_page(request):
	context={
	"title" :"RT Register"
	}
	#print(request.user.is_authenticated)
	return render(request,"register.html",get_index_parms(context))

def check_out_page(request):
	context={
	"title" :"Home"
	}
	#print(request.user.is_authenticated)
	return render(request,"check-out.html",get_index_parms(context))

def faq_page(request):
	context={
	"title" :"Home"
	}
	#print(request.user.is_authenticated)
	return render(request,"faq.html",get_index_parms(context))

def product_page(request):
	context={
	"title" :"Home"
	}
	#print(request.user.is_authenticated)
	return render(request,"product.html",get_index_parms(context))


def shopping_cart_page(request):
	context={
	"title" :"Home"
	}
	#print(request.user.is_authenticated)
	return render(request,"shopping-cart.html",get_index_parms(context))
