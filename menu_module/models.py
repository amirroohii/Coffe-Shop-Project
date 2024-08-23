from django.db import models

# Create your models here.

class Menu(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    title = models.CharField(max_length=350, db_index=True)
    url_title = models.CharField(max_length=350, db_index=True)
    is_active = models.BooleanField(null=True)
    is_delete = models.BooleanField()

    def __str__(self):
        return self.title


class Product(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='products_menu')
    title = models.CharField(max_length=200)
    url_title = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/products', null=True, blank=False)
    short_description = models.CharField(max_length=200)
    is_active = models.BooleanField(null=True)
    is_delete = models.BooleanField(null=True)

    def __str__(self):
        return f'({self.title} - {self.url_title})'




