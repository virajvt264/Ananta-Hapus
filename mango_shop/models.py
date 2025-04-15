from django.db import models
from django.db.models import Model, EmailField
from django.conf import settings

# Create your models here.
class Product(models.Model):
    product_id =models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    small_desc = models.CharField(max_length=200, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    pub_date = models.DateField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    product_weight = [
        ("200", "200g"),
        ("250", "250g"),
        ("300", "300g")
    ]
    weight = models.CharField(max_length=10, choices=product_weight, default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, default="")
    email = models.EmailField(max_length=90, default="")
    phone = models.TextField(max_length=30, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=90)
    state = models.CharField(max_length=100)
    zip_code = models.TextField(max_length=10)
    phone = models.TextField(max_length=30, default="")

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[:7] + "..."
