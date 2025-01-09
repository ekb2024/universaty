
from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=False,null=True)
    age = models.CharField(max_length=3)

#
class  Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=3 ,decimal_places=2, blank=False,null=True)
    size =  models.DecimalField(max_digits=500, decimal_places=1, blank=False,null=True)
    description = models.TextField()
    age_limited = models.BooleanField()
    buyer = models.ManyToManyField(Buyer)
    buyer_1 = models.DecimalField(max_digits=5, decimal_places=5, blank=False,null=True)
    buyer_2 = models.BooleanField()
