from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)
    country_code = models.CharField(max_length=25, null = True)
    temperature = models.DecimalField(max_digits=30, decimal_places=3,default = 0)
    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'