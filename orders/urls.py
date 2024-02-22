from django.urls import path

from .views import fetch_customer_orders, fetch_ordered_products_by_period, fetch_ordered_products_by_days
from .views import fetch_order_list, fetch_order, create_order, add_customer_products

urlpatterns = [
    path('customer-orders/<int:customer_id>', fetch_customer_orders, name='customer_orders'),
    path('ordered-products-by-period/<int:customer_id>', fetch_ordered_products_by_period,
         name='ordered_products_by_period'),
    path('ordered-products-by-days/<int:customer_id>/<int:num_days>', fetch_ordered_products_by_days,
         name='ordered_products_by_days'),
    path('list/', fetch_order_list, name='order_list'),
    path('<int:order_id>/', fetch_order, name='order_view'),
    path('create/', create_order, name='create_order'),
    path('<int:order_id>/add/', add_customer_products, name='add_customer_products'),
]
