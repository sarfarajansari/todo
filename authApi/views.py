from rest_framework.decorators import api_view
from rest_framework.response import Response
from .emailVerify import valid,SendMailWithHtml
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import  authenticate
from django.template.loader import render_to_string
from .models import*
from random import randint
from store.models import Order
from .models import ClayStudent


@api_view(["POST"])
def register(request):
    data = request.data
    if "email" in data and "username" in data and "password1" in data and "password2" in data and "Fname" in data and "Lname" in data:
        try:
            user = User.objects.get(email=data["email"])
            return Response({"message":"User already exist!","status":1})
        except:
            pass
        form = UserCreationForm(data)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.email = data["email"]
            user.first_name = data["Fname"]
            user.last_name = data["Lname"]
            user.save()
            token = Token.objects.get(user=user).key
            if "session" in data:
                session = data["session"]
                if "completed_orders" in session:
                    for i in session["completed_orders"]:
                        try:
                            order= Order.objects.get(pk=i)
                            if not order.customer:
                                order.customer = user
                                order.save()
                        except:
                            print("could not add orders")
                if "orderId" in data:
                    try:
                        order = Order.objects.get(pk = int(session["orderId"]))
                        if not order.customer:
                                order.customer = user
                                order.save()
                    except:
                        pass

                session={}
                            
            return Response({"message":"Registered","status":0,"token":token,"session":session})
        else:
            error=""
            for f in form.errors.values():
                for g in f:
                    error=g
                    break;
            responseData ={"status":1}
            if error:
                responseData={
                    "message":error,
                    "status":1
                }
                print(error)

            return Response(responseData)
    return Response({"message":"invalid information provided!","status":1})

@api_view(["POST"])
def login(request):
    data = request.data
    if "type" in data:
        if str(data["type"])=="1":
            if "username" in data and "password" in data:
                username = data["username"]
                password = data["password"]
                if valid(username):
                    try:
                        user = User.objects.get(email=username)
                        print(user.password,password)
                        u= authenticate(username=user.username,password=password)
                        if u is not None:
                            token = Token.objects.get(user=user).key
                            return Response({"status":0,"message":"Logged in successfully.","token":token})
                        else:
                            return Response({"status":1,"message":"Invalid username or password."})
                    except:
                        return Response({"status":1,"message":"User does not exist.Please signup!"})

                user = authenticate(username=username, password=password)
                if user is not None:
                    try:
                        token = Token.objects.get(user=user).key
                        return Response({"status":0,"message":"Logged in successfully.","token":token})
                    except:
                        return Response({"status":1,"message":"User not found."})
                else:
                    return Response({"status":1,"message":"Invalid username or password."})
            return Response({"status":1,"message":"Invalid information."})
        elif str(data["type"])=="2":
            if "email" in data:
                email = data["email"]
                print(email)
                try:
                    user = User.objects.filter(email=email).first()
                    token = Token.objects.get(user=user).key
                    return Response({"status":0,"message":"Logged in successfully.","token":token})
                except:
                    return Response({"status":1,"message":"User does not exist.Please signup!"})
            return Response({"status":1,"message":"Invalid information."})

    return Response({"status":1,"message":"Invalid information."})

@api_view(["POST"])
def otpapi(request):
    data = request.data
    if "email" in data:
        email = data["email"]
        if valid(email):
            otp = randint(100000, 999999)
            text = render_to_string("email/otp.html",{"otp":otp})
            SendMailWithHtml(email, text,'one time password')
            return Response({"status":0,"message":"OTP sent","otp":otp})
        else:
            return Response({"status":1,"message":"Invalid Email"})
    return Response({"status":1,"message":"Invalid Information provided"})


@api_view(["GET"])
def check(request):
    if request.user.is_authenticated:
        try: 
            student = ClayStudent.objects.get(student=request.user)
            return Response({"status":"0"})
        except:
            pass
    return Response({"status":"1"})