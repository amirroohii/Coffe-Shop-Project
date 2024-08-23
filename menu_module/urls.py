from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductMenuView.as_view(), name='product_menu')
]