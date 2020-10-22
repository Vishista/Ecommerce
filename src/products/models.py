from django.db import models
import random
import os
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.urls import reverse
from django.db.models import Q

# Create your models here.

def get_file_extension(filepath):

    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    print(instance)
    print(filename)
    new_file_name = random.randint(0,555555555)
    name,ext = get_file_extension(filename)
    final_name = '{new_file_name}{ext}'.format(new_file_name=new_file_name,ext=ext)
    return "products/{new_file_name}/{final_name}".format(
        new_file_name=new_file_name,
        final_name=final_name
        )

class NewQuerySet(models.query.QuerySet):

    def active(self):
        return self.filter(active =True)

    def featured(self):
        return self.filter(featured=True, active = True)

    def search(self,query):
       lookup = (Q(title__icontains=query) |
                 Q(description__icontains=query) |
                 Q(price__icontains=query)  |  
                 Q(tag__title__icontains=query)) 
       return self.filter(lookup).distinct()
        #return self.filter(featured=True)

class ProductManager(models.Manager):
    # def all(self):
    #     return self.get_queryset().active()

    def get_queryset(self):
        return NewQuerySet(self.model, using= self._db)
        #return None

    def featured(self):
      return self.get_queryset().filter(featured=True)  

    def get_by_id(self,id):
      qs =  self.get_queryset().filter(id=id)
      if qs.count()==1:
        return qs.first()
      else:
        return None
    def search(self,query):
      return self.get_queryset().active().search(query)



class Product(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(blank = True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0.00)
    image = models.ImageField(upload_to = upload_image_path, default = 'null')
    featured = models.BooleanField(default = False)
    active = models.BooleanField(default = True)
    timestamp = models.DateTimeField(auto_now_add = True)


    objects = ProductManager()

    def __str__(self):
      return self.title

    @property
    def name(self):
      return self.title
    

    def get_absolute_url(self):
     #  return "/product/{slug}/".format(slug=self.slug)
     return reverse('product:details', kwargs={'slug' : self.slug})

def pre_save_receiver(sender, instance, *args, **kwargs):
        if not instance.slug:
           instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender= Product)

