from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='image_products', null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
class Product(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='image_products')
    description = models.TextField()
    price = models.IntegerField(null=True)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title