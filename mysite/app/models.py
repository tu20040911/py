from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
#register
class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','first_name','last_name','password1','password2']

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)

    def __str__(self) :
        return self.name
class money_item(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
    money = models.CharField(max_length=200,null=True)
    def __str__(self) :
        return self.money
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    digital = models.BooleanField(default=False,null=True,blank=False)
    image = models.ImageField(null=True,blank=True)
    def __str__(self) :
        return self.name
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = " "
        return url     
class Video18(models.Model):
    name = models.CharField(max_length=200,null=True)
    LINK = models.CharField(max_length=200,null=True)
    Mota = models.CharField(max_length=200,null=True)
    digital = models.BooleanField(default=False,null=True,blank=False)
    image = models.ImageField(null=True,blank=True)
    def __str__(self) :
        return self.name
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = " "
        return url     
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
class ShippingAddress(models.Model):
    Customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    mobile = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.address