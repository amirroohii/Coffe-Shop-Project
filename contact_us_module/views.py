from django.shortcuts import render, redirect
from django.views.generic import FormView

from site_module.models import SiteSetting
from .forms import ContactUsForm


# Create your views here.
# class ContactUsView(FormView):
#     template_name = 'contact_us_module/contact_us.html'
#     form_class = ContactUsForm
#     success_url = '/contact-us/'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#

def contact_us(request):
    form = ContactUsForm()
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()

    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-us')

    return render(request, 'contact_us_module/contact_us.html', context={'form': form, 'site_setting': setting})


