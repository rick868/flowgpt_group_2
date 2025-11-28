from django.contrib import admin
from .models import Category, Supplier, Product, Customer, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    ordering = ['name']
    list_per_page = 20


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_info', 'address']
    search_fields = ['name', 'contact_info', 'address']
    ordering = ['name']
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock_quantity', 'supplier', 'date_added']
    list_filter = ['category', 'supplier', 'date_added']
    search_fields = ['name', 'description']
    ordering = ['name']
    list_per_page = 25
    list_select_related = ['category', 'supplier']

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'stock_quantity', 'category')
        }),
        ('Supplier Information', {
            'fields': ('supplier',)
        }),
    )

    autocomplete_fields = ['category', 'supplier']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'date_joined']
    list_filter = ['date_joined']
    search_fields = ['name', 'email', 'phone_number']
    ordering = ['name']
    list_per_page = 20


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total_price', 'status', 'payment_method', 'order_date']
    list_filter = ['status', 'payment_method', 'order_date']
    search_fields = ['customer__name', 'id']
    ordering = ['-order_date']
    list_per_page = 25
    list_select_related = ['customer']

    # Fields to display in detail view
    fieldsets = (
        ('Order Information', {
            'fields': ('customer', 'status', 'payment_method')
        }),
        ('Financial Information', {
            'fields': ('total_price',)
        }),
        ('Timestamps', {
            'fields': ('order_date',),
            'classes': ('collapse',)
        }),
    )

    # Custom action
    actions = ['mark_as_completed']

    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status='COMPLETED')
        self.message_user(request, f'{updated} orders marked as completed.')

    mark_as_completed.short_description = "Mark selected orders as completed"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity', 'price', 'get_total_price']
    list_filter = ['order__order_date']
    search_fields = ['product__name', 'order__id']
    ordering = ['-id']
    list_per_page = 25
    list_select_related = ['order', 'product']

    def get_total_price(self, obj):
        return obj.quantity * obj.price

    get_total_price.short_description = 'Total Price'

    autocomplete_fields = ['order', 'product']