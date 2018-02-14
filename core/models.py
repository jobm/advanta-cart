from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
class Product(TimeStampedModel):
    name = models.CharField(verbose_name="Name of Product", max_length=100, blank=True)
    image = models.ImageField(verbose_name="Image Path to Product", upload_to="product_photos/", blank=True)
    description = models.TextField(verbose_name="Description of Product", blank=True)
    price = models.FloatField(verbose_name="Price of Product", blank=True, default="0.00")
    on_sale = models.BooleanField(verbose_name="Product on Sale", default=False)
