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

class commonTypes(models.Model):
    typeName    = models.CharField(max_length=120)
    description = models.TextField()
    useImage    = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.typeName


class common(models.Model):

    Name = models.CharField(max_length=120)
    value = models.CharField(max_length=120)
    value1 = models.CharField(max_length=120,null=True, blank=True)
    value2 = models.CharField(max_length=120,null=True, blank=True)
    value3 = models.CharField(max_length=120,null=True, blank=True)
    typeName = models.ForeignKey(commonTypes,on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name