from django.db import models


class Service(models.Model):
    area=models.IntegerField()
    bedrooms=models.IntegerField()
    age=models.IntegerField()
    info=models.TextField()
    value=models.DecimalField(decimal_places=4,max_digits=9999999999999 , default=0)



# Create your models here.
