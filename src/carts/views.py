from django.shortcuts import render
from .models import Cart,CartCount
from products.models import Product
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.

def test(request):
    number = 2
    #return HttpResponse(number)
    return render(request, 'products/prod_add.html', {'count': number})

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj


def cart_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    # print(total)
    cart_obj.total = total
    cart_obj.save()
 
   
    return render(request, 'carts/cart_display.html', {"cart": cart_obj })



def cart_update(request):
    print(request.POST.get('product_id'))
    product_id = request.POST.get('product_id')
    context = {}
    if product_id is not None:
        try:
           product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotexist:
            print("product is not there")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
           cart_obj.products.remove(product_obj)
           
        else:

           cart_obj.products.add(product_obj)
           no_of_items = cart_obj.products.all().count()
           CartCount.nr_of_prod = no_of_items
           context = {
              'no_of_items' : no_of_items
           }
        #return redirect(product_obj.get_absolute_url())
        return redirect("cart:home")
       # return render(request, 'carts/cart_display.html',context)


