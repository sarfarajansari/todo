from django.urls import path
from . import views




urlpatterns=[
    #api
    path("api/orderapi/",views.OrderApi,name="order"),
    path("api/order/history/",views.OrdersHistory,name="OrderHistory"),
    path("api/update/product/<str:action>/<int:pk>/",views.OrderUpdate,name="update_order"),
    path("api/products/",views.ProductListApi,name="produuctlist"),
    path("api/submit/order/",views.SubmitOrder,name="submit_order"),
    path("api/completed/order/<int:pk>",views.CompletedOrder,name="completed_order"),
    path("api/product/<int:pk>/",views.ProductApi,name="productapi"),
    path("api/message/",views.message,name="message"),


]

