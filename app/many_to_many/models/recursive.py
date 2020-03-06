from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    similar_products = models.ManyToManyField('self')

    def __str__(self):
        return self.name
