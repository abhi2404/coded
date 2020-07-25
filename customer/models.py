from django.db import models
from registration.models import user, shopkeeper


# Create your models here.
class shoppinglist(models.Model):
<<<<<<< HEAD
    item = models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True,blank=True)
    # key=models.ForeignKey('',models.DO_NOTHING
=======
    pt = models.ForeignKey('user.name', on_delete="DO_NOTHING", null = True)
    shp = models.ForeignKey('shopkeeper.name', on_delete="DO_NOTHING", null = True)
    item = models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True,blank=True)
    # key=models.ForeignKey('',models.DO_NOTHING)
>>>>>>> d77c8f17a2ae35f3f7df9eab3215b105e2dbcfe1
    Status=models.CharField(max_length=20,default="pending")