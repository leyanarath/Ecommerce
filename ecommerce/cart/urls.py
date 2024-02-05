from django.urls import path
from . import views
app_name='cart'
urlpatterns=[
    path('add/<int:pro_id>/',views.add_cart,name="add_cart"),
    path('',views.cart_detail,name="cart_detail"),
    path('remove/<int:pro_id>/',views.cart_remove,name="cart_remove"),
    path('del/<int:pro_id>/',views.fullremove,name="fullremove"),
]