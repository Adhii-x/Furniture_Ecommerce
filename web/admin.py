from django.contrib import admin

from .models import Blog, Order, OrderItem, Product

# Register your models here.




class Orderitems(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [Orderitems]


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('user','price','image')
    list_filter = ('name','price','image')


@admin.register(Blog)
class Product(admin.ModelAdmin):
    list_display = ('name','tittle','image','')
    search_fields = ('user',)

@admin.register(Order)
class Product(admin.ModelAdmin):
    list_display = ('user','first_name','last_name','country','address','city','state','pincode','phone','email','date')
    search_fields = ('user',)



@admin.register(OrderItem)
class Product(admin.ModelAdmin):
    list_display = ('order','Product','image','quantity','price','total','paid')
    search_fields = ('user','Product')

admin.site.register(Order, OrderAdmin)