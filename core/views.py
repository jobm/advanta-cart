from django.views.generic import ListView
from .models import Product


# Create your views here.
class ListProducts(ListView):
    template_name = "core/index.html"

    def get_queryset(self):
        return Product.objects.filter(on_sale=True)
