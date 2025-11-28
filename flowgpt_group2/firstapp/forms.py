from django import forms
from .models import Category, Supplier, Product, Customer, Order, OrderItem

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info', 'address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def _init_(self, *args, **kwargs):
        super(ProductForm, self)._init_(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number', 'address']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'total_price', 'status', 'payment_method']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price']
