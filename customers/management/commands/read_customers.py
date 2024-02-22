from django.core.management.base import BaseCommand
from customers.models import Customer


class Command(BaseCommand):
    help = "Read all customers"

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        # для красивого вывода построчно, а не в виде QuerySet
        for customer in customers:
            self.stdout.write(str(customer))
