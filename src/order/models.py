from django.db import models
from products.models import Product

# Create your models here.


class ProductPurchase:
    
    prodlist = {}

    # def __init__(self, prod):
    #     self.__prodlist = prod
    
    def set_prod(self, prodnew):
        
        self.prodlist = prodnew

    def get_prod(self):
        
        return self.prodlist


    




# class ProductPurchase:
#     global prod_list 
#     prod_list = {}
#     def set_product_purchase(self,context):
#         print(context['product_list'])
#         prod_list = context['product_list']
#         print(prod_list)
#     def get_product_purchase(self):
#         print(prod_list)
#         return prod_list

# class ProductPurchase:
#     def set_product_purchase(self,request):
#         print('i am here')
        

#     def get_product_purchase(self):
#         return self.prod_list

class OrderManager(models.Manager):
    prod_list = {} 
    context = {}
    def create_order(self,user):
        order = self.create(user=user)
        return order

    


        # prod_list = context['product_list']
        # for product in self.context['product_list']:
        #   print(product.title)

   


class Order(models.Model):
    
    user = models.CharField(max_length = 100)
    products = models.ManyToManyField(Product, blank= True)
    address  = models.CharField(max_length = 500)
    total = models.DecimalField(default = 0.00, max_digits= 100 , decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add = True)
    phone = models.CharField(max_length = 20)


    objects = OrderManager()














