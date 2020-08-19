from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
	rate = models.PositiveIntegerField()
	name = models.CharField(max_length = 20)
	created_date = models.DateField(default=datetime.now)

	def __str__(self):
		return self.name

class Billing(models.Model):
	quantity = models.PositiveIntegerField()
	balance_amt = models.FloatField()
	product = models.ForeignKey(Product,on_delete = models.DO_NOTHING)