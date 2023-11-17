from django.contrib import admin
from core import models
# Register your models here.

admin.site.register(models.AddOn)
admin.site.register(models.Category)
admin.site.register(models.Item)
admin.site.register(models.ItemImage)
admin.site.register(models.Restaurant)
admin.site.register(models.Review)
admin.site.register(models.SubAddOn)
admin.site.register(models.Order)
admin.site.register(models.RestaurantCategory)



