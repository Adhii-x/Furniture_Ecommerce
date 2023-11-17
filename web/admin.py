from django.contrib import admin

from .models import Blog, Order, OrderItem, Product

# Register your models here.




@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ('name','price',)
    list_filter = ('name','price',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name','tittle',)


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product','quantity',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    fields = ("product","quantity", "image", "price", "total", "paid")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',)
    search_fields = ('user',)
    inlines=[OrderItemInline]
    
    


