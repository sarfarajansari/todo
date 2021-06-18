from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    digital=models.BooleanField(default=False,null=True)
    image= models.ImageField(null=True,blank=True,upload_to='store')
    type = models.CharField(blank=True,null=True,default="",max_length=200)   
    weight = models.CharField(blank=True,null=True,default="",max_length=200)
    dimensions = models.CharField(blank=True,null=True,default="",max_length=200)

    @property
    def get_images(self):
        return self.images.all()

    @property
    def get_details(self):
        return self.details.all()


    @property
    def getWeight(self):
        return self.weight + " Kilogram"
    
    def __str__(self):
        return self.name


class ProductDetails(models.Model):
    detail = models.CharField(blank=True,null=True,max_length=999)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="details")

class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    date_orderer=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=True)
    transaction_id= models.CharField(max_length=200,null=True)
    total = models.FloatField(default=0)

    def __str__(self):
        if self.customer:
            return self.customer.get_full_name() + " : " + str(self.pk)
        return str(self.id)

    
    
    @property
    def items(self):
        return self.orderitem_set.all()
    @property
    def total_amount(self):
        total = 0
        items= self.orderitem_set.all()
        for item in items :
            total+= item.product.price
        return total

    @property
    def shipping(self):
        shipping = False
        items= self.orderitem_set.all()
        for item in items :
            if  item.product.digital==False:
                shipping=True
                break
        return shipping



    @property
    def get_cart_total(self):
        total=0
        for item in self.orderitem_set.all():
            total+=item.get_item_total

        return total

    @property
    def get_total_items(self):
        total_item=0
        for item in self.orderitem_set.all():
            total_item+=item.quantity
        return total_item


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    order= models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    quantity= models.IntegerField(default=1,null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_item_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name

    

class ShippingAddress(models.Model):
    customer=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    order= models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address= models.CharField(max_length=200,null=True)
    city= models.CharField(max_length=200,null=True)
    state= models.CharField(max_length=200,null=True)
    zipcode= models.CharField(max_length=200,null=True)
    country= models.CharField(max_length=200,null=True,default="")

    @property
    def strAddress(self):
        return f"{self.address}"
    def __str__(self):
        return f" {self.city} , {self.state} "

class Images(models.Model):
    img = models.ImageField(null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")

    def __str__(self):
        return self.product.name +" : " + str(self.img)




class Message(models.Model):
    name= models.CharField(max_length=80)
    email = models.CharField(max_length=200)
    text = models.CharField(max_length=999)

    def __str__(self):
        return self.name + " : "+ self.text