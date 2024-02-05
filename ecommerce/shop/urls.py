from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    path('',views.AllProdCat,name="AllProdCat"),
    path('<slug:c_sulg>/',views.AllProdCat,name="AllProdCatgory"),
    path('<slug:c_sulg>/<slug:Product_sulg>/',views.proDetail,name="ProdCatDatail")
]