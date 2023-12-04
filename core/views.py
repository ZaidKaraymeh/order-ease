from django.shortcuts import render
from core import models
# Create your views here.

def home(request):

    retaurant_categories = models.RestaurantCategory.objects.filter(is_enabled = True)

    context = {
        "categories": retaurant_categories
    }

    return render(request, "home.html", context)

def search(request):
    return render(request, "home.html")

def resturant(request):
    return render(request, "resturant.html")