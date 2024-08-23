from django.shortcuts import render, get_object_or_404
from .models import Product, Menu
# Create your views here.
from django.views.generic import TemplateView

class ProductMenuView(TemplateView):
    template_name = 'menu_module/menu_components.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_menu = Menu.objects.filter(is_active=True, parent__isnull=False).all()
        context['product_menu'] = products_menu
        return context

