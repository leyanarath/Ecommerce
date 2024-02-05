from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# def index(request):
#     return HttpResponse("jhcbdsj")
def AllProdCat(request,c_sulg=None):
    c_page=None
    products_list=None
    if c_sulg!=None:
        c_page=get_object_or_404(Category,slug=c_sulg)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,"category.html",{"category":c_page,"products":products})
def proDetail(request,c_sulg,Product_sulg):
    try:
        product=Product.objects.get(category__slug=c_sulg,slug=Product_sulg)
    except Exception as e:
        raise e
    return render(request,'product.html',{'Product':product})