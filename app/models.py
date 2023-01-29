from django.db import models

# Create your models here.



class Galary(models.Model):
    iid = models.CharField(max_length=100,null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return self.name

   