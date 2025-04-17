from django.db import models
from django.contrib.auth.models import User

class CustomerDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # new
    address_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, default="")
    email = models.EmailField(max_length=90, default="")
    address = models.CharField(max_length=150, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    zip_code = models.CharField(max_length=10, default="")
    phone = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name


