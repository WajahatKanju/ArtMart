from django.shortcuts import render
from products.models import Category


# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "shop/index.html", context)
