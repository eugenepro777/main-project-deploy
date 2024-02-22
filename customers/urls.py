from django.urls import path

from .views import add_customer, fetch_customer, fetch_customer_list, edit_customer

urlpatterns = [
    path('list/', fetch_customer_list, name='customer_list'),
    path('<int:customer_id>/', fetch_customer, name='customer_view'),
    # path('edit/', edit_customer, name='edit_customer'),
    path('add/', add_customer, name='add_customer'),
]