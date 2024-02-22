from django.core.management.base import BaseCommand
from orders.models import Order
from customers.models import Customer
from products.models import Product
from django.utils import timezone


class Command(BaseCommand):
    help = "Create a new order"

    def handle(self, *args, **kwargs):
        customer = Customer.objects.order_by('?').first()
        products = Product.objects.order_by('?')[:3]
        total_amount = sum(product.price for product in products)
        order_date = timezone.now().date()
        order = Order(
            customer=customer,
            total_amount=total_amount,
            order_date=order_date,
        )
        order.save()
        order.products.set(products)
        self.stdout.write(self.style.SUCCESS(f'Successfully created order: {order}'))
