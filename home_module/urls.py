from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index_page, name='home')
    path('', views.IndexPageView.as_view(), name='home')
]
