# """
# URL configuration for HotelBooking project.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from database.views import home,Providerstorage,Customerstorage, login, locationsearch, all, hotel_details, requestdata, accept_request
# from database.views import edit_hotel, delete_image, accept_history
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',home),
#     path('Providerstorage/',Providerstorage),
#     path('Customerstorage/',Customerstorage),
#     path('login/',login),
# path("locationsearch/", locationsearch, name="locationsearch"),
# path("all/", all, name="all"),
# path("hotel_details/<int:id>/",hotel_details, name="hotel_details"),
# path("requestData/<int:id>/",requestdata, name="requestdata"),
# path('accept-request/<int:id>/<str:email>/<int:u_id>/', accept_request, name='accept_request'),
# path("edit_hotel/<int:id>/", edit_hotel, name="edit_hotel"),
# path("delete_image/<int:img_id>/", delete_image, name="delete_image"),
# path('accept_history/<int:id>/',accept_history, name='accept_history'),
# ]
#
#
from django.contrib import admin
from django.urls import path
from database.views import home, Providerstorage, Customerstorage, login, locationsearch, all, hotel_details, requestdata, accept_request
from database.views import edit_hotel, delete_image, accept_history, hotel_chat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('Providerstorage/', Providerstorage),
    path('Customerstorage/', Customerstorage),
    path('login/', login),
    path("locationsearch/", locationsearch, name="locationsearch"),
    path("all/", all, name="all"),
    path("hotel_details/<int:id>/", hotel_details, name="hotel_details"),
    path("requestData/<int:id>/", requestdata, name="requestdata"),
    path('accept-request/<int:id>/<str:email>/<int:u_id>/', accept_request, name='accept_request'),
    path("edit_hotel/<int:id>/", edit_hotel, name="edit_hotel"),
    path("delete_image/<int:img_id>/", delete_image, name="delete_image"),
    path('accept_history/<int:id>/', accept_history, name='accept_history'),
    path("chat/", hotel_chat, name="hotel_chat"),
]