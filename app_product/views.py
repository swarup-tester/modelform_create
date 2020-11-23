from django.shortcuts import render, redirect
from django.contrib import messages

from app_product.forms import ProductForm

# Create your views here.

def create(request):
    form = ProductForm()           # Object for the ModelForm

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            messages.success(request, f'{name} got successfully registered')
            return redirect('create')
        else:
            messages.success(request, ('Fill all the inputs.'))
            return redirect('create')
    
    return render(request,'app_product/create.html',context={'form_obj':form})
    

