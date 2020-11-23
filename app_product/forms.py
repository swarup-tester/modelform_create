from django import  forms
from app_product.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','remark','email','image']
