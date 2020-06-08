from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.email
class User1(models.Model):
    username = models.OneToOneField(Customer,on_delete=models.CASCADE,null=True,blank=True)
    email = models.CharField(max_length=200,null=True)

class stock(models.Model):


    pname = models.CharField(max_length=32)
    quan =  models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.pname

    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.pname

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)





    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
	product = models.ForeignKey(stock, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
