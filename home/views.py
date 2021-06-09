from .models import Website,Message
from .authentication import SendMailWithHtml
from django.template.loader import render_to_string
import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import WebsiteClass,PageClass


@api_view(["GET"])
def projectsApi(request):
    websitesobjects = Website.objects.all()
    websites = []
    for web in websitesobjects:
        webdata = WebsiteClass(web).data
        webdata["image"] ="/static"+str( web.get_homepage.img.url)
        websites.append(webdata)
    return Response(websites)

@api_view(["GET"])
def projectApi(request,pk):
    try:
        website = Website.objects.get(pk=pk)
    except:
        return Response({"status":1,"message":"Project Not found"})
    data = WebsiteClass(website).data
    try:
        pages=[]
        for page in website.get_pages:
            pages.append(PageClass(page).data)
        data["pages"]=pages
    except:
        return Response({"status":1,"message":"Pages Not found"})
    return Response({"status":0,"message":"Project found","website":data}) 

@api_view(["POST"])
def messageApi(request):
    P = request.data
    if "name" in P and "email" in P and "msg" in P:
        name = P["name"]
        email = P["email"]
        msg = P["msg"]
        mess = Message.objects.create(name=name,email=email,message=msg,time = datetime.datetime.now())
        SendMailWithHtml(render_to_string("email.html",{"msg":mess}))
        return Response({"status":0,"message":"Message sent"})
    return Response({"status":1,"message":"Invalid Message"})
