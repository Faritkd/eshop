from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.http import Http404
from django.views.generic.base import TemplateView
from django.views.generic import ListView


# Create your views here.
class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(is_active=True)
        return data


class ProductDetailView(TemplateView):
    template_name = 'product_module/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        context['product'] = product
        return context

