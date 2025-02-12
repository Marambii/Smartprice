from django.urls import path
from . import views

app_name = 'pricefinder' 

urlpatterns = [
    path('', views.landing_page, name='landing_page'), 
    path('search/', views.product_search, name='product_search'), 
    path('details/<int:product_id>/', views.product_details, name='product_details'), 
]