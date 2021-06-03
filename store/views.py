from django.shortcuts import redirect
from .models import*
import datetime,random , string
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer,OrderItemSerializer,OI,Cart,CartSerializer,ImageSerializer,DeatailsSerializer,ShippingAddressSerializer,UserClass,UserSerializer

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


# Basic Functions
def get_order(request,session):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(
            customer=request.user, complete=False)
        return order,session
    else:
        if "orderId" in session:
            try:
                order = Order.objects.get(pk=session["orderId"])
                return order,session
            except:
                order = Order(complete=False)
                order.save()
                session["orderId"] = order.id
                return order,session
        else:
            order = Order(complete=False)
            order.save()
            session["orderId"] = order.id
            print("created new order")
            if "completed_orders" not in session:
                session["completed_orders"] = []
            return order,session

def get_completed_orders(request,session):
    if request.user.is_authenticated:
        orders= Order.objects.filter(
            customer=request.user, complete=True)
        print(orders)
        return orders
    else:
        if "completed_orders" in session:
            try:
                completed_orders = session["completed_orders"]
                orders = []
                for i in completed_orders:
                    orders.append(Order.objects.get(pk=i))
                return orders
            except:
                pass
        return []


# APIs
@api_view(['GET'])
def ProductListApi(request):
    products = Product.objects.all()
    products = list(reversed(products))
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def ProductApi(request,pk):
    if "session" not in request.data:
        return Response({"status":1,"message":"invalid information"})
    
    # getting product
    try:
        product = Product.objects.get(pk=pk)
    except:
        return Response({"status":1})
    Data = ProductSerializer(product).data

    # getting details
    try:
        details = ProductDetails.objects.filter(product=product)
        Data["details"]=DeatailsSerializer(details,many=True).data
    except:
        pass

    # getting images
    try:
        images = Images.objects.filter(product=product)
        Data["images"]=ImageSerializer(images,many=True).data
    except:
        pass
    order,session = get_order(request,request.data["session"])
    try:
        orderitem = OrderItem.objects.get(order=order,product=product)
        Data["quantity"]=orderitem.quantity
    except:
        Data["quantity"]=0
    Data["status"]=0
    return Response(Data)

@api_view(['POST'])
def OrderUpdate(request,action,pk):
    print(action,pk)
    if "session" not in request.data:
        return Response({"status":1,"message":"invalid information"})
    order,session = get_order(request,request.data["session"])
    
    try:
        product = Product.objects.get(pk=pk)
    except:
        return Response({"message":"Product not found","status":1},status=404)
    try:
        orderitem = OrderItem.objects.get(product=product,order=order)

        if action=="add":
            orderitem.quantity+=1

        elif action == "remove":
            orderitem.quantity-=1
            if orderitem.quantity==0:
                orderitem.delete()
                return Response({"message":"Product Removed from cart!","session":session,"status":0})
        else:
            return Response({"message":"undefined action","status":1})
        orderitem.save()
        return Response({"message":"Cart updated : " + str(product.name)+" x "+str(orderitem.quantity),"session":session,"status":0})
    except:
        if action == "add":
            orderitem = OrderItem(order=order,product=product,quantity=1)
            orderitem.save()
            return Response({"message":"Product added to cart!","session":session,"status":0})

@api_view(['POST'])
def OrderApi(request):
    if "session" not in request.data:
        return Response({"status":1,"message":"invalid information"})
    order,session = get_order(request,request.data["session"])
    cart = Cart(order)
    Data = CartSerializer(cart).data

    orderitems = order.orderitem_set.all()
    newlist=[]
    for item in orderitems:
        newlist.append(OI(item))
    Data["orderitems"] = OrderItemSerializer(newlist, many=True).data
    Data["session"]=session
    return Response(Data)

@api_view(['POST'])
def SubmitOrder(request):
    if "session" not in request.data:
        return Response({"status":1,"message":"invalid information"})
    session = request.data["session"]
    data=request.data
    if request.user.is_authenticated:
        try:
            customer = request.user
        except:
            return Response({"message":"user not found","status":1})
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
    else:
        try:
            customer, created = User.objects.get_or_create(
                first_name=data["Fname"],last_name=["Lname"], email=data["email"],username = get_random_string(16),password=get_random_string(16))
            customer.save()
            order = Order.objects.get(pk=session["orderId"])
            order.customer = customer
            order.save()
        except:
            return Response({"message":"user not found","status":1})

    order.total = order.total_amount
    order.transaction_id = datetime.datetime.now().timestamp()
    shippingAddress = ShippingAddress(
        customer=customer,
        order=order,
        address=data["address"],
        city=data["city"],
        state=data["state"],
        zipcode=data["zipcode"],
        country=data["country"]
    )
    order.complete = True
    order.date = datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(hours=5,minutes=30)
    order.save()
    shippingAddress.save()
    if not request.user.is_authenticated:
        session["completed_orders"].append(
            session["orderId"])
        del session["orderId"]
    
    return Response({"message":"order submitted","status":0,"session":session})

@api_view(['POST'])
def OrdersHistory(request):
    if "session" not in request.data:
        return Response({"status":1,"message":"invalid information"})
    orders = get_completed_orders(request,request.data["session"])
    carts = []
    for order in orders:
        carts.append(Cart(order))
    carts = list(reversed(carts))
    serializer = CartSerializer(carts,many=True)
    return Response(serializer.data)

@api_view(["POST"])
def CompletedOrder(request,pk):
    print(request.data)
    if "session" not in request.data:
        return Response({"status":1,"message":"invalid information"})
    orders = get_completed_orders(request,request.data["session"])
    order =False
    
    for i in orders:
        if i.id ==pk:
            order = i
            break
    if order:
        cart = Cart(order)
        Data = CartSerializer(cart).data

        orderitems = order.orderitem_set.all()
        newlist=[]
        for item in orderitems:
            newlist.append(OI(item))
        Data["orderitems"] = OrderItemSerializer(newlist, many=True).data
        
        try:
            shipping = ShippingAddress.objects.get(order=order)
            Data["shipping"]=ShippingAddressSerializer(shipping).data
            Data["status"]=0
            return Response(Data)
        except:
            pass
    return Response({"status":1})
        
@api_view(["POST"])
def message(request):
    data = request.data
    if "name" in data and "email" in data and "text" in data:
        msg = Message(name = data["name"],email= data["email"],text=data["text"])
        msg.save()
        return Response({"message":"Message Received!","status":0})
    return Response({"message":"Invalid information provided!","status":1})


