from django.shortcuts import render
from carts.models import Cart
from .models import Order
from .models import Product
from .models import ProductPurchase
from userdetails.models import UserInfo

# Create your views here.

   

def order_view(request):
    print(request.GET)
    return render(request, 'order/order_details.html', {})

def single_order(request):
    print(request.POST)
    prod_id = request.POST.get('product_id')
    global prod_list
    prod_list = Product.objects.none()
    global single_prod
    #context['item']  =  request.POST.get('product')
    #context['total']  = context['item'].price
    single_prod = Product.objects.get(id=prod_id)
    
    context = {
     'item' : single_prod,
     'total' : single_prod.price
    }
    return render(request, 'order/order_summary.html', context)

def order_summary(request):
    print(request.POST)
    id = request.POST.get('cart')
    username = request.user.username
    print(username)
    qs = UserInfo.objects.filter(user= username)
    #print(qs)
    if qs.exists():
     address = qs.first().address
    else:
     address = 'enter address'

    obj = Cart.objects.get(id=id)
    product_list = obj.products.all()
    total = obj.total
    print(total)
    
    # for product in product_list:
    #   print(product.title)

    context = {
        'product_list': product_list,
        'total': total,
        'address': address

    }
    global prod_list
    prod_list = context['product_list']
    # prods = context['product_list']
    # a = ProductPurchase()
    # b = ProductPurchase()
    # print('before')
    # ProductPurchase.get_prod()
    # ProductPurchase.set_prod(prods)
    # print('after')
    # ProductPurchase.get_prod()
    #a.set_prod(context)
    # print('before')
    # print(a.get_prod())
    # print(b.get_prod())
    # a.set_prod(prods)
    # print('after')
    # print(a.get_prod())
    # print(b.get_prod())
    #ProductPurchase.prodlist = context['product_list']
    #a.set_product_purchase(context)
    #a.set_prodlist(context['product_list'])
    return render(request, 'order/order_summary.html', context)

def order_pay(request):
    #prod_list = request.POST.get('product_list')
    #prod_list2 = Product(prod_list)
    # print(prod_list)
    # print(Product.objects.all())
    # print(request.user)
    
    new_order = Order.objects.create_order(user=str(request.user))
    # b = ProductPurchase()
    # prod_list= ProductPurchase.prodlist
    # prod_list= b.get_prod()
    global prod_list
    global single_prod
    if prod_list.exists() :
        for product in prod_list:
            print('hi')
            print(product)
            new_order.products.add(product)
    else:
        new_order.products.add(single_prod)
    new_order.total = request.POST.get('total')
    new_order.address = request.POST.get('address')
    
    new_order.phone = '03326511974' 

    new_order.save()

    return render(request, 'order/pay.html', {})


def saved_orders(request):
    print(request.POST)
    id = request.POST.get('order_id')
    #orders = Order.objects.filter(user=str(request.user))
    #sorted_order = orders.order_by('-timestamp')
    #print(orders)
    order = Order.objects.get(id=id)
    orders = Order.objects.all().order_by('-timestamp')
    print(id)
    context = {
     'order': order,
     'orders': orders
    }
    return render(request,'order/saved_order.html', context)

def order_list(request):
    orders = Order.objects.filter(user=str(request.user))
    sorted_order = orders.order_by('-timestamp')
    print(orders)
    context = {
     'orders': sorted_order
    }
    return render(request,'order/order_list.html', context)
