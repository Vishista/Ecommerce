from django.conf.urls import url


from .views import (
   order_view,
   order_summary,
   order_pay,
   saved_orders,
   single_order,
   order_list

)


#app_name = 'products'

urlpatterns = [
 url(r'^$', order_view, name = 'home'),
  url(r'^summary$', order_summary, name = 'summary'),
  url(r'^pay$', order_pay, name = 'pay'),
  url(r'^savedorders$', saved_orders, name = 'saved'),
  url(r'^single$', single_order, name = 'single'),
  url(r'^list$', order_list, name = 'list'),

 
]