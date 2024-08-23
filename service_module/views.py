from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.views.generic import FormView
# Create your views here.

# class ServiceView(FormView):
#     template_name = 'service_module/service.html'
#     form_class = ReservationForm
#     success_url = '/service/'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(kwargs)
#         context['form'] = self.form_class

def service(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('service')

        else:
            form = ReservationForm()
            form.errors
            return redirect('service')

    return render(request, 'service_module/service.html', {'form': form})

