from django.conf.urls import url


from .views import (
    # product_list,
    ProdList,
    # product_details,
    # ProdDetail,
    # ProdFeaturedList,
    # ProdFeaturedDetail,
    ProdSlug,	

)


#app_name = 'products'

urlpatterns = [
 url(r'^$', ProdList.as_view(), name = 'list'),
 #url(r'^pcv$', ProdList.as_view()),
 # url(r'^featured$', ProdFeaturedList.as_view()),
 # url(r'^pcv/(?P<pk>\d+)/$', ProdDetail.as_view()),
 # url(r'^featured/(?P<pk>\d+)/$', ProdFeaturedDetail.as_view()),
 url(r'^(?P<slug>[\w-]+)/$', ProdSlug.as_view(), name = 'details'),
 # url(r'^$', product_list),
 # url(r'^(?P<nr>\d+)/$', product_details),
 
 
]