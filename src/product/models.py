# Create your models here.
from django.db import models
import os
from django.core.validators import MaxValueValidator,MinValueValidator
#from datetime import  datetime
import random
#from .utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.urls import reverse

def get_filename_ext(filepath):
    base_name   = os.path.basename(filepath)
    name,ext    = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    className=instance.__class__.__name__
    print(className)
    name,ext        = get_filename_ext(filename)
    final_filemane  = f'{instance.name}{ext}'
    if className=="productImage":
        productName=product.objects.filter(id=instance.product).first().name
        return f"{className}/{productName}/{final_filemane}"
    else:
        return f"{className}/{instance.name}/{final_filemane}"


class color(models.Model):
    color       = models.CharField(max_length=120)
    colorCode   = models.CharField(max_length=120)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.color

class size(models.Model):
    size        = models.CharField(max_length=120)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.size

class brand(models.Model):
    name        = models.CharField(max_length=120)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class catageory(models.Model):

    name            = models.CharField(max_length=120)
    description     = models.TextField()
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    image           = models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return self.name


class subCatageory(models.Model):

    catageoryId           = models.ForeignKey(catageory,on_delete=models.CASCADE)
    name                = models.CharField(max_length=120)
    description         = models.TextField()
    active              = models.BooleanField(default=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    image               = models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return str(self.catageoryId)+','+self.name


class ProductQuerySet(models.query.QuerySet):
    # def featured(self):
    #     return self.filter(featured=True)

    def active(self):
        return self.filter(active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)

    def get_by_id(self,id):
        qs=self.get_queryset().filter(id=id).active()
        if qs.count() !=1:
            return qs.first()
        else:
            return qs
        return None

    # def featured(self):
    #     return self.get_queryset().filter(featured=True).active()

    def all(self):
        return self.get_queryset().active()

class product(models.Model):
    #subCatageory=subCatageory()
    name                = models.CharField(max_length=120)
    catageoryId         = models.ForeignKey(catageory,on_delete=models.CASCADE)
    subCatageoryId      = models.ForeignKey(subCatageory,on_delete=models.CASCADE)
    brand               = models.ForeignKey(brand,on_delete=models.CASCADE)
    ProductRate         = models.IntegerField(default=0, validators=[MaxValueValidator(9999999), MinValueValidator(1)])
    shortDescription    = models.TextField()
    longDescription     = models.TextField()
    Introduction        = models.TextField()
    active              = models.BooleanField(default=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    image               = models.ImageField(upload_to=upload_image_path)

    objects = ProductManager()

    def __str__(self):
        return str(self.subCatageoryId)+','+self.name

class productSerial(models.Model):

    ProductSerial       = models.CharField(max_length=120)
    catageoryId           = models.ForeignKey(catageory, on_delete=models.CASCADE)
    subCatageoryId        = models.ForeignKey(subCatageory, on_delete=models.CASCADE)
    product             = models.ForeignKey(product, on_delete=models.CASCADE)
    color               = models.ForeignKey(color, on_delete=models.CASCADE)
    size                = models.ForeignKey(size, on_delete=models.CASCADE)
    mrp                 = models.IntegerField(default=0,validators=[MaxValueValidator(9999999),MinValueValidator(1)])
    purchaseDate        = models.DateTimeField()
    active              = models.BooleanField(default=True)
    timestamp           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)+','+self.ProductSerial




class productImage(models.Model):
    name                = models.CharField(max_length=120)
    catageoryId         = models.ForeignKey(catageory, on_delete=models.CASCADE)
    subCatageoryId      = models.ForeignKey(subCatageory,  on_delete=models.CASCADE)
    product             = models.ForeignKey(product, on_delete=models.CASCADE)
    productSerial       = models.ForeignKey(productSerial, on_delete=models.CASCADE)
    image               = models.ImageField(upload_to=upload_image_path)
    active              = models.BooleanField(default=True)
    timestamp           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)+','+self.name

class offers(models.Model):

    name            = models.CharField(max_length=120)
    catageoryId       = models.ManyToManyField(catageory)
    subCatageoryId    = models.ManyToManyField(subCatageory)
    product         = models.ManyToManyField(product)
    percentage      = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    fromDate        = models.DateTimeField()
    toDate          = models.DateTimeField()
    maxDiscount     = models.IntegerField(default=0, validators=[MaxValueValidator(999999), MinValueValidator(0)])

    def __str__(self):
        return self.name


