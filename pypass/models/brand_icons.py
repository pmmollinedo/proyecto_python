from django.db import models


class BrandIcons(models.Model):
    id_brand_icon = models.BigAutoField(primary_key=True)
    brand_name = models.CharField(max_length=50)
    brand_icon = models.CharField(max_length=100)
