from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.name
