from django.http import HttpRequest
from django.shortcuts import render, redirect
from contact_us_module.forms import ContactUsForm
from menu_module.models import Menu
from site_module.models import SiteSetting, SiteFooterLink
# Create your views here.
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['setting'] = setting
        products_menu = Menu.objects.filter(is_active=True, parent__isnull=False).all()
        context['product_menu'] = products_menu
        return context


def site_header_components(request: HttpRequest):
    return render(request, 'shared/site_header_components.html')

def site_footer_components(request: HttpRequest):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_items = SiteFooterLink.objects.all()
    instagram = footer_items.filter(title__iexact='instagram').first()
    x = footer_items.filter(title__iexact='twitter').first()

    context = {
        'site_setting': setting,
        'footer_items': footer_items,
        'instagram': instagram,
        'twitter': x,
    }

    return render(request, 'shared/site_footer_components.html', context)
