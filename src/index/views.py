from django.shortcuts import render,redirect
from customModels.models import common,commonTypes
from product.models import (catageory,
                            subCatageory,
                            product,
                            productSerial,
                            productImage,
                            offers)

def index_page(request):
	#get common Types Id
	logoid=commonTypes.objects.filter(typeName='logo').first().id
	paymentMethodid=commonTypes.objects.filter(typeName='paymentMethod').first().id
	emailid=commonTypes.objects.filter(typeName='email').first().id
	phoneid=commonTypes.objects.filter(typeName='phone').first().id
	addressid=commonTypes.objects.filter(typeName='address').first().id
	bannerid=commonTypes.objects.filter(typeName='banner').first().id
	heroid = commonTypes.objects.filter(typeName='hero').first().id

	# get querysets
	logoQuerySet=common.objects.filter(typeName=logoid)
	paymentMethodQuerySet=common.objects.filter(typeName=paymentMethodid)
	emailQuerySet=common.objects.filter(typeName=emailid)
	phoneQuerySet=common.objects.filter(typeName=phoneid)
	addressQuerySet=common.objects.filter(typeName=addressid)
	bannerQuerySet=catageory.objects.all()
	heroQuerySet = common.objects.filter(typeName=heroid)
	prodList={}
	for c in bannerQuerySet:
		print(c.name)
		#print(subCatageory.objects.filter(catageoryId=c.id).all())
		#print(product.objects.filter(catageoryId=c.id).all())
		prodList[c]={'subCategory':subCatageory.objects.filter(catageoryId=c.id).all(),
					 'product':product.objects.filter(catageoryId=c.id)[:2].all()}

	#get Objects
	headerLogo=logoQuerySet.filter(Name__icontains='headerLogo').order_by('Name').first()
	footerLogo=logoQuerySet.filter(Name__icontains='footerLogo').order_by('Name').first()
	partnerLogo=logoQuerySet.filter(Name__icontains='partnerLogo').order_by('Name').all()
	paymentMethodLogo=paymentMethodQuerySet.filter(Name='paymentMethod').order_by('Name').first()
	email=emailQuerySet.filter(Name__icontains='email').order_by('Name').first()
	phone=phoneQuerySet.filter(Name__icontains='phone').order_by('Name').first()
	address=addressQuerySet.filter(Name__icontains='address').order_by('Name').first()
	bannerLogo=bannerQuerySet
	heroLogo=heroQuerySet.order_by('Name').all()

	#MainlogUrl=common.objects.filter(Name='headerLogo',typeName=logoid).first().image.url
	context={
		"MainLogo" :"Home Page",
		#"MainlogUrl": MainlogUrl,
		"headerLogo" : headerLogo,
		"footerLogo" : footerLogo,
		"partnerLogo":partnerLogo,
		"paymentMethodLogo":paymentMethodLogo,
		"email":email,
		"phone":phone,
		"address":address,
		"bannerLogo":bannerLogo,
		"heroLogo":heroLogo,
		"prodList":prodList
	}

	#print(common.objects.raw("select * from customModels_common  where Name='MainLogo'"))
	#print(prodList)
	return render(request,"index.html",context)

def login_page(request):
	context={
	"title" :"Home Page"
	}
	#print(request.user.is_authenticated)
	return render(request,"login.html",context)

def contact_page(request):
	context={
	"title" :"Home Page"
	}
	#print(request.user.is_authenticated)
	return render(request,"contact.html",context)

def register_page(request):
	context={
	"title" :"Home Page"
	}
	#print(request.user.is_authenticated)
	return render(request,"register.html",context)

def blog_page(request):
	context={
	"title" :"Home Page"
	}
	#print(request.user.is_authenticated)
	return render(request,"blog.html",context)

def blog_details_page(request):
	context={
	"title" :"Home Page"
	}
	#print(request.user.is_authenticated)
	return render(request,"blog-details.html",context)

def check_out_page(request):
	context={
	"title" :"Home Page"
	}
	#print(request.user.is_authenticated)
	return render(request,"check-out.html",context)

def faq_page(request):
	context={
	"title" :"Home Page"
	}
	#print(request.user.is_authenticated)
	return render(request,"faq.html",context)

def product_page(request):
	context={
	"title" :"Home Page"
	}
	#print(request.user.is_authenticated)
	return render(request,"product.html",context)

def shop_page(request):
	context={
	"title" :"Home Page"
	}
	#print(request.user.is_authenticated)
	return render(request,"shop.html",context)

def shopping_cart_page(request):
	context={
	"title" :"Home Page"
	}
	#print(request.user.is_authenticated)
	return render(request,"shopping-cart.html",context)