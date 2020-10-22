from django.db import models
from django.contrib.auth.models import User

class UserInfoManager(models.Manager):
  def create_userinfo(self,user,address,email,phone):
    userinfo = self.create(user=user,address=address,email=email,phone=phone)  
    userinfo.save
    return userinfo
# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    email = models.EmailField(blank = True)
    phone = models.CharField(max_length = 200, blank = True)

    objects = UserInfoManager()