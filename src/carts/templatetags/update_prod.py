from django import template
from carts.models import Cart,CartCount
register = template.Library()




@register.filter(name='prod_add')
def prod_add(count,user):
	
	cart = Cart.objects.filter(user=user).last()
	count = cart.products.all().count()
	
	return count