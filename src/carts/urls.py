from django.conf.urls import url


from .views import (
    # product_list,
    cart_view,
 
    cart_update,	
    test
)


#app_name = 'products'

urlpatterns = [
 

 url(r'^$', cart_view, name = 'home'),
 url(r'^update/$', cart_update, name = 'update'),
 url(r'^test/$', test, name = 'test'),
 
 
]