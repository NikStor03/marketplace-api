from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name='home'),
    path('add-product/', views.add_items, name='add-product'),
    path('all/', views.all_products, name='view-products'),
    path('edit-product/<int:pk>/', views.edit_products, name='edit-product'),
    path('edit-product-price/<int:pk>/', views.edit_products_price, name='edit-product-price'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete-product'),
    path('calculate-product-prices/<int:pk>/', views.calculate_product_prices, name='calculate-product-prices'),
    path('product-changes/<int:pk>/', views.product_changes, name='product-changes'),
]
