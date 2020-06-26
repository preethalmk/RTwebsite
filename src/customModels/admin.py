from django.contrib import admin

# Register your models here.

from .models import commonTypes,common

# class commonInLine(admin.StackedInline):
#     model = common.typeName
#     extra = 1

class CommonTypesAdmin(admin.ModelAdmin):
    # inline = [commonInLine]
    list_display= ['__str__']
    class Meta:
        model=commonTypes

class CommonAdmin(admin.ModelAdmin):
    list_display= ['__str__']
    class Meta:
        model=common


admin.site.register(commonTypes,CommonTypesAdmin)
admin.site.register(common,CommonAdmin)
