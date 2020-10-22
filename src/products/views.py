from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.db.models.signals import pre_save, post_save
from carts.models import Cart




class ProdSlug(DetailView):
    queryset = Product.objects.all()
    template_name = "products/prod_details.html"

    def get_context_data(self,*args,**kwargs):
        context = super(ProdSlug,self).get_context_data(*args,**kwargs)
        request = self.request
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
          instance = Product.objects.get(slug=slug,active=True)
          print(instance)
           # if instance is None:
           # raise Http404("the object does not exists")
        except Product.DoesNotExist:
            raise Http404("product does not exist")
        
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("i dont know ")

        return instance

class ProdFeaturedList(ListView):
    queryset = Product.objects.all().featured()
    #queryset = Product.objects.featured()
    #queryset = Product.objects.all()

  
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProdFeaturedDetail(DetailView):
    queryset = Product.objects.all().featured()
    #queryset = Product.objects.featured()
    template_name = "products/featured_details.html"
  
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

class ProdList(ListView):
    #queryset = Product.objects.all()

    # def get_context_data(self,*args,**kwargs):
    #     context = super(ProdList,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return(context)
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()



def product_list(request):

    obj = Product.objects.all()
    print(obj)
    context = {
       'object_list' : obj
    }
    # context = {
    #   'form' : form
    # }
    return render(request, "products/prod_list.html", context)

class ProdDetail(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/prod_details.html"
    
    # def get_context_data(self,*args,**kwargs):
    #     context = super(ProdDetail,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return(context)

    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("the object does not exists")
        return instance
     
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     qs = Product.objects.filter(id=pk)
    #     return qs




def product_details(request, nr, *args, **kwargs):
    #obj = Product.objects.all()
   # obj = Product.objects.get(id=pk)
   # print(kwargs)
    #print(kwargs)
    #obj2 = get_object_or_404(Product,id=nr)
    # try:
    #     qs = Product.objects.get(id=nr)
    # except Product.DoesNotExist:
    #     print("object does not exist")
    #     raise Http404("product does not exist")
    # context = {
    #    'object' : qs
    # }
    #instance = Product.objects.get(id = nr, featured=True)
   # qs2 = Product.objects.filter(id = nr)
    instance = Product.objects.get_by_id(nr)
   # instance = Product.objects.filter(id = nr, featured = True)
    #print(instance)
    #prod = instance.first()
    # print(qs1)
    # print(qs2)
    #if qs2.exists() and qs2.count()==1:
    #     print(" object exists")
        # instance = qs2.first(()
    #if instance.count()==1:
    if instance is None:
       raise Http404("the object does not exists")
    context = {
      'object' : instance
    }
      # context = {
      #     'object' : instance.first()
      #   }
    #else:
    #  raise Http404("the object does not exists") 
    return render(request, "products/prod_details.html", context)

   


    

