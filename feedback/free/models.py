from django.db import models

# Create your models here.


class FeedBack(models.Model):

    experience = models.CharField(max_length=200)
    comprehensiveness = models.CharField(max_length=200)
    price_rate = models.CharField(max_length=200)
    order_delivery = models.CharField(max_length=200)
    customer_support = models.CharField(max_length=200)
    recommend = models.CharField(max_length=200)
    expectations = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.experience

