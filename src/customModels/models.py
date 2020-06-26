from django.db import models

# Create your models here.
from django.db import models
import os
import random
#from .utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.urls import reverse

def get_filename_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    print(instance)
    print(filename)
    #new_filename=random.randint(1,100)
    name,ext=get_filename_ext(filename)
    final_filemane=f'{instance.Name}{ext}'
    return f"common/{instance.typeName}/{final_filemane}"

class CustomQuerySet(models.query.QuerySet):
    # def featured(self):
    #     return self.filter(featured=True)

    def active(self):
        return self.filter(active=True)

class CustomModelManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model,using=self._db)

    def get_by_id(self,id):
        qs=self.get_queryset().filter(id=id).active()
        if qs.count() !=1:
            return qs.first()
        else:
            return qs
        return None

    def first(self):
        return self.get_queryset().active().first()

    # def featured(self):
    #     return self.get_queryset().filter(featured=True).active()

    def all(self):
        return self.get_queryset().active().all()

class commonTypes(models.Model):
    typeName    = models.CharField(max_length=120,unique=True)
    description = models.TextField()
    useImage    = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CustomModelManager()

    def __str__(self):
        return f"{self.id}-{self.typeName}"


class common(models.Model):

    Name = models.CharField(max_length=120,unique=True)
    value = models.CharField(max_length=120)
    value1 = models.CharField(max_length=120,null=True, blank=True)
    value2 = models.CharField(max_length=120,null=True, blank=True)
    value3 = models.CharField(max_length=120,null=True, blank=True)
    typeName = models.ForeignKey(commonTypes,on_delete=models.CASCADE,related_name='common')
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CustomModelManager()

    def __str__(self):
        return f"{self.id}-{self.typeName}-{self.Name}"
