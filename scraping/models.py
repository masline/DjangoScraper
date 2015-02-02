from django.db import models

# Create your models here.


class Price(models.Model):
	price = models.DecimalField(max_digits=20, decimal_places=10)
	per = models.IntegerField()


class Data(models.Model):
	item = models.CharField(max_length=50)  # The part number
	manu = models.CharField(max_length=50)  # The name of the manufacturer
	scraped = models.DateTimeField(auto_now_add=True)  # The date & time this value was scraped
	pricing = models.ManyToManyField(Price)