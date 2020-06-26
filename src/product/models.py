# Create your models here.
from django.db import models
import os
from django.core.validators import MaxValueValidator,MinValueValidator
#from datetime import  datetime
import random
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
#from .utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.urls import reverse
from customModels.models import CustomModelManager
from datetime import datetime

def get_filename_ext(filepath):
    base_name   = os.path.basename(filepath)
    name,ext    = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    className=instance.__class__.__name__
    print(className)
    name,ext        = get_filename_ext(filename)
    prefix          = str(datetime.now().strftime('%d%m%Y%H%M%S%f'))
    final_filemane  = f'{instance.name}{prefix}{ext}'
    if className=="productImage":
        productName=product.objects.filter(id=instance.product.id).first().name
        return f"{className}/{productName}/{final_filemane}"
    else:
        return f"{className}/{instance.name}/{final_filemane}"


class color(models.Model):
    color       = models.CharField(max_length=120)
    colorCode   = models.CharField(max_length=120)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    objects = CustomModelManager()
    def __str__(self):
        return f"{self.id} - {self.color} ({self.colorCode})"

class size(models.Model):
    name        = models.CharField(max_length=120,default='Size')
    size        = models.CharField(max_length=120)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    objects = CustomModelManager()
    def __str__(self):
        return f"{self.size}"

class brand(models.Model):
    name        = models.CharField(max_length=120)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CustomModelManager()

    def __str__(self):
        return f"{self.name}"


class catageory(models.Model):

    name            = models.CharField(max_length=120)
    description     = models.TextField()
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    image           = models.ImageField(upload_to=upload_image_path)
    largeImage      = models.ImageField(upload_to=upload_image_path,blank=True)

    objects = CustomModelManager()

    def __str__(self):
        return f"{self.name}"


class subCatageory(models.Model):

    catageoryId         = models.ForeignKey(catageory,on_delete=models.CASCADE,related_name='subcatageory')
    name                = models.CharField(max_length=120)
    description         = models.TextField()
    active              = models.BooleanField(default=True)
    default             = models.BooleanField(default=False)
    timestamp           = models.DateTimeField(auto_now_add=True)
    image               = models.ImageField(upload_to=upload_image_path)

    objects = CustomModelManager()

    def __str__(self):
        return f"cat({self.catageoryId}) {self.id} - {self.name}"

class product(models.Model):
    #subCatageory=subCatageory()
    name                = models.CharField(max_length=120)
    subCatageoryId      = models.ForeignKey(subCatageory,on_delete=models.CASCADE,related_name='product')
    brand               = models.ForeignKey(brand,on_delete=models.CASCADE)
    ProductRate         = models.IntegerField(default=0, validators=[MaxValueValidator(9999999), MinValueValidator(1)])
    shortDescription    = models.TextField()
    longDescription     = models.TextField()
    Introduction        = models.TextField()
    active              = models.BooleanField(default=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    image               = models.ImageField(upload_to=upload_image_path)

    objects = CustomModelManager()

    def save(self):
        super().save()  # saving image first
        img = Image.open(self.image.path) # Open image using self
        new_img = (300, 300)
        img.thumbnail(new_img)
        img.save(self.image.path)

    def __str__(self):
        return self.name

class productSerial(models.Model):

    ProductSerial       = models.CharField(max_length=120)
    product             = models.ForeignKey(product, on_delete=models.CASCADE,related_name='productserial')
    color               = models.ForeignKey(color, on_delete=models.CASCADE)
    size                = models.ForeignKey(size, on_delete=models.CASCADE)
    mrp                 = models.IntegerField(default=0,validators=[MaxValueValidator(9999999),MinValueValidator(1)])
    purchaseDate        = models.DateTimeField()
    active              = models.BooleanField(default=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    objects = CustomModelManager()

    def __str__(self):
        return str(self.product)+','+self.ProductSerial




class productImage(models.Model):
    name                = models.CharField(max_length=120)
    product             = models.ForeignKey(product, on_delete=models.CASCADE,related_name='productimage')
    image               = models.ImageField(upload_to=upload_image_path)
    thumbnail           = models.ImageField(upload_to=upload_image_path, editable=False)
    active              = models.BooleanField(default=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    objects             = CustomModelManager()

    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')
        super(productImage, self).save(*args, **kwargs)

    def make_thumbnail(self):
        image = Image.open(self.image)
        image.thumbnail((140,140), Image.ANTIALIAS)
        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()
        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False    # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()
        return True

    def __str__(self):
        return str(self.product)+','+self.name

class offers(models.Model):

    name            = models.CharField(max_length=120)
    catageoryId       = models.ManyToManyField(catageory,related_name='offers')
    subCatageoryId    = models.ManyToManyField(subCatageory,related_name='offers')
    product         = models.ManyToManyField(product,related_name='offers')
    percentage      = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    fromDate        = models.DateTimeField()
    toDate          = models.DateTimeField()
    maxDiscount     = models.IntegerField(default=0, validators=[MaxValueValidator(999999), MinValueValidator(0)])
    objects = CustomModelManager()

    def __str__(self):
        return self.name
