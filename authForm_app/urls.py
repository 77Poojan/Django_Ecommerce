from django.contrib import admin
from django.urls import path
from myApp import views as mv
from authForm_app import views as av

urlpatterns = [
    path('', av.sign_up,name='signup'),
    path('userlogin/',av.user_login,name='userlogin'),
    path('userprofile/',av.user_profile,name='userprofile'),
    path('userlogout/',av.user_logout,name='userlogout'),
    path('changepass/',av.user_changepass,name='changepass'),
    path('', mv.store, name="store"),
	path('cart/', mv.cart, name="cart"),
	path('checkout/', mv.checkout, name="checkout"),
	path('update_item/', mv.updateItem, name="update_item"),
	path('process_order/', mv.processOrder, name="process_order"),    
]

