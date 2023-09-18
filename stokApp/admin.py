from django.contrib import admin
from django.utils.html import format_html
# from django.contrib.auth.admin import UserAdmin
from .models import Category, Product, Brand, Firm, Purchases, Sales

# Register your models here.

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Brand)
# admin.site.register(Firm)
# admin.site.register(Purchases)
# admin.site.register(Sales)

#--------

class FirmAdmin(admin.ModelAdmin):
    list_display = ('display_image', 'name', 'phone', 'address')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return 'Resim Yok'

    display_image.allow_tags = True
    display_image.short_description = 'Resim'
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('display_image','name')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return 'Resim Yok'

    display_image.allow_tags = True
    display_image.short_description = 'Resim'
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('display_image','name')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return 'Resim Yok'

    display_image.allow_tags = True
    display_image.short_description = 'Resim'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('display_image', 'name', 'category', 'brand', 'stock')

    def display_image(self, obj):
        if obj.brand.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.brand.image.url)
        else:
            return 'Resim Yok'

    display_image.allow_tags = True
    display_image.short_description = 'Resim'
    
class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('display_image','user', 'firm', 'brand', 'product', 'price_total', )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return 'Resim Yok'

    display_image.allow_tags = True
    display_image.short_description = 'Resim'
   
class SalesAdmin(admin.ModelAdmin):
    list_display = ('display_image','user', 'brand', 'price_total', 'quantitiy')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return 'Resim Yok'

    display_image.allow_tags = True
    display_image.short_description = 'Resim'    
    
    
    
# class CustomUserAdmin(UserAdmin):
#     list_display = ("image", 'display_image')

#     def display_image(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
#         else:
#             return 'Resim Yok'

#     display_image.allow_tags = True
#     display_image.short_description = 'Profil Resmi'



 


admin.site.register(Firm, FirmAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Purchases, PurchasesAdmin)
admin.site.register(Sales, SalesAdmin)

# admin.site.register(CustomUser, CustomUserAdmin)







