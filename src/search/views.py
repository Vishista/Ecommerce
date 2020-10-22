from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


# Create your views here.

class SearchProdView(ListView):
    #queryset = Product.objects.all()
    template_name = 'search/list.html'
    def get_context_data(self,*args,**kwargs):
         context = super(SearchProdView,self).get_context_data(*args,**kwargs)
         context['prod'] = self.request.GET.get('q')
         return context
    #     print(context)
    #     return(context)
    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('q', None)
       
        if query is not None:
          return Product.objects.search(query)
       
        return Product.objects.featured()