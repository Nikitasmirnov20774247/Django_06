from django.contrib import admin
from .models import Customer, Product, Order


@admin.action(description="Сбросить количество продукта в ноль")
def reset_product_quantity(modeladmin, request, queryset):
    queryset.update(product_quantity=0)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'address', 'date_reg']
    list_filter = ['name', 'email', 'date_reg']
    search_fields = ['name', 'email', 'phone', 'date_reg']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'product_quantity','date_add']
    list_filter = ['name', 'price', 'date_add']
    search_fields = ['name', 'price', 'product_quantity', 'date_add']
    readonly_fields = ['date_add']
    actions = [reset_product_quantity]
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["name"],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'product_quantity'],
            },
        ),
        (
            'Прочее',
            {
                'fields': ['date_add', 'image'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'order_date']
    list_filter = ['customer', 'total_price', 'order_date']
    search_fields = ['customer', 'total_price', 'order_date']
    readonly_fields = ['order_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['total_price'],
            },
        ),
        (
            'Состав заказа',
            {
                'classes': ['collapse'],
                'fields': ['product'],
            }
        ),
        (
            "О заказе",
            {
                "fields": ['customer', 'order_date']
            }
        ),
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
