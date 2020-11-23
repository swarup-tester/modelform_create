from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30,verbose_name="Enter Product Name")
    price = models.IntegerField(verbose_name="Enter Price")
    remark = models.CharField(max_length=30,verbose_name="Enter Remark")
    email = models.EmailField(max_length=254,verbose_name="Enter Email")
    image = models.ImageField(upload_to='pic_upload',verbose_name="Upload Image")