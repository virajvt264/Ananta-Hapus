from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='Mango_shop-home'),
    path('about/', views.about, name='Mango_shop - AboutUs'),
    path('contact/', views.contact, name='Mango_shop - ContactUs'),
    path('tracking/', views.tracking, name='Mango_shop - TrackingStatus'),
    path('product/<int:myid>', views.product, name='Mango_shop - ProductView'),
    path('checkout/', views.checkout, name='Mango_shop - CheckOut'),
    path('gallary/', views.gallary, name='Mango_shop - Gallary'),
    path('search/', views.search, name='Mango_shop - search'),
    path('products/', views.products, name='Mango_shop - products'),
    # path('meva/', views.meva, name='Mango_shop - Meva'),
]
