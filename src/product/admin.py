from django.contrib import admin
from django import forms

# Register your models here.
from .models import color,size,brand,catageory,subCatageory ,product,productSerial,productImage,offers

# class LockAdminForm(forms.ModelForm):
#   class Meta:
#     model = product
#     exclude = ()
#
#   def __init__(self, *args, **kwargs):
#     super(LockAdminForm, self).__init__(*args, **kwargs)
#     my_model = self.instance
#     print(subCatageory.objects.filter(catageoryId=my_model.catageoryId))
#     self.fields['subCatageoryId'].queryset = subCatageory.objects.filter(catageoryId=my_model.catageoryId.id)


class colorAdmin(admin.ModelAdmin):
    list_display= ['__str__']
    class Meta:
        model=color

class sizeAdmin(admin.ModelAdmin):
    list_display= ['__str__']
    class Meta:
        model=size

class brandAdmin(admin.ModelAdmin):
    list_display= ['__str__']
    class Meta:
        model=brand

class catageoryAdmin(admin.ModelAdmin):
    list_display= ['__str__']
    class Meta:
        model=catageory

class subCatageoryAdmin(admin.ModelAdmin):
    list_display= ['__str__']
    class Meta:
        model=subCatageory

# class subCatageoryAdmin(admin.ModelAdmin):
#     list_display= ['__str__']
#     form = LockAdminForm
#     #filter_horizontal = ('catageoryId',)
#     #class Meta:
#     #    model=subCatageory

class productAdmin(admin.ModelAdmin):
    list_display= ['__str__']
    class Meta:
        model=product

class productSerialAdmin(admin.ModelAdmin):
    list_display= ['__str__']
    class Meta:
        model=productSerial

class productImageAdmin(admin.ModelAdmin):
    list_display= ['__str__']
    class Meta:
        model=productImage

class offersAdmin(admin.ModelAdmin):
    list_display= ['__str__']
    class Meta:
        model=offers


admin.site.register(color,colorAdmin)
admin.site.register(size,sizeAdmin)
admin.site.register(brand,brandAdmin)
admin.site.register(catageory,catageoryAdmin)
admin.site.register(subCatageory,subCatageoryAdmin)
admin.site.register(product,productAdmin)
admin.site.register(productSerial,productSerialAdmin)
admin.site.register(productImage,productImageAdmin)
admin.site.register(offers,offersAdmin)