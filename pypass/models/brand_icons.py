from django.db import models


class BrandIcons(models.Model):
    id_brand_icon = models.BigAutoField(primary_key=True)
    brand_name = models.CharField(max_length=50)
    brand_icon_class = models.CharField(max_length=100)
    brand_importance_order = models.IntegerField(default=3)
    is_activated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.brand_name}'
