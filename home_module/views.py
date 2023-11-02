from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import TemplateView

from product_module.models import Product
from site_module.models import SiteSetting, FooterLinkBox, Slider
from utils.convertors import group_list


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        context['sliders'] = sliders
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')
        most_visit_products = Product.objects.filter(is_delete=False, is_active=True).annotate(visit_count=Count('productvisit')).order_by('-visit_count')[:12]
        context ['most_visit_products'] = group_list(most_visit_products)
        context['latest_products'] = group_list(latest_products)
        return context


def site_header_component(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {'site_setting': setting}
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set
    context = {'site_setting': setting, 'footer_link_boxes': footer_link_boxes}
    return render(request, 'shared/site_footer_component.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context
