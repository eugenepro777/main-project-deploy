from django.urls import path

from .views import add_product, fetch_product, fetch_product_list, edit_product

urlpatterns = [
    path('add/', add_product, name='add_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('list/', fetch_product_list, name='product_list'),
    path('<int:product_id>/', fetch_product, name='product_view'),
]
