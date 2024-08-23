from . import views
from django.urls import path

urlpatterns = [
    path('', views.service, name='service')
    # path('', views.ServiceView.as_view(), name='service')
]