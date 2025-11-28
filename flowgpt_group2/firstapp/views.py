from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm

# Create your views here.

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')  # Redirect after successful save
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})