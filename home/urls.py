from django.urls import include, path
from . import views

urlpatterns = [
    path('ajax/load-rate/', views.load_products, name='ajax_load_rates'),  # <-- this one here
    path('bill/',views.get_bil,name='get_bill')
]