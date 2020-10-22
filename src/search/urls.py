from django.conf.urls import url


from .views import (
    
    SearchProdView,
   
  
)


#app_name = 'products'

urlpatterns = [
 url(r'^$', SearchProdView.as_view(), name = 'query'),

 
 
]