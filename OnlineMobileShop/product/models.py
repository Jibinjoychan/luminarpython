from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.brand_name

class Mobile(models.Model):
    mobile_name=models.CharField(max_length=120,unique=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    ram=models.CharField(max_length=120)
    price=models.IntegerField()
    camera=models.CharField(max_length=120)
    os=models.CharField(max_length=120)
    image=models.ImageField(upload_to="images")

    def __str__(self):
        return self.mobile_name

class Orders(models.Model):
    personname=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    pin=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    productid=models.IntegerField()
    user=models.CharField(max_length=15)
    choice=(
        ('orderreceived','orderreceived'),
        ('dispatched','dispatched'),
        ('delivered','delivered')
    )
    status=models.CharField(max_length=120,choices=choice,default="orderreceived")
    active_status=models.IntegerField(default=1)
    def __str__(self):
        return self.personname
