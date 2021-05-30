from rest_framework import serializers
from .models import Product,Images,ProductDetails,ShippingAddress
from django.contrib.auth.models import User


class DeatailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductDetails
        fields=["detail"]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Images
        fields=["img"]
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OI:
    def __init__(self,OI):
        self.orderitemId = OI.id
        self.order = OI.order.id
        self.quantity = OI.quantity
        self.product = OI.product.id
        self.name = OI.product.name
        self.price = OI.product.price
        self.image = OI.product.image
        self.total = OI.get_item_total  

class OrderItemSerializer(serializers.Serializer):
    orderitemId = serializers.IntegerField()
    order = serializers.IntegerField()
    quantity = serializers.IntegerField()
    product= serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()
    image = serializers.ImageField()
    total = serializers.IntegerField()

class Cart:
    def __init__(self,obj):
        self.total=obj.get_cart_total
        self.item = obj.get_total_items
        self.id = obj.id
        self.date = obj.date_orderer.date()

class CartSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    id = serializers.IntegerField()
    date = serializers.DateField()
    item = serializers.IntegerField()


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ["address","city","state","zipcode","country"]


class UserClass:
    def __init__(self,user):
        self.pk = user.id
        self.name = user.get_full_name()
        self.email=user.email
        self.username=user.username
class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.CharField()
    username = serializers.CharField()



