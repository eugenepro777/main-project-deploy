from datetime import timedelta
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404

from .forms import OrderForm
from .models import Customer, Order


def fetch_order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def fetch_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})


def fetch_customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    context = {
        'customer': customer,
        'orders': orders,
    }
    return render(request, 'orders/orders.html', context)


# сортировка товаров из заказов - за неделю, месяц, год
def fetch_ordered_products_by_period(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    year_ago = today - timedelta(days=365)

    orders_week = Order.objects.filter(customer=customer, order_date__gte=week_ago)
    orders_month = Order.objects.filter(customer=customer, order_date__gte=month_ago)
    orders_year = Order.objects.filter(customer=customer, order_date__gte=year_ago)

    products_week = set()
    products_month = set()
    products_year = set()

    for order in orders_week:
        products_week.update(order.products.all())

    for order in orders_month:
        products_month.update(order.products.all())

    for order in orders_year:
        products_year.update(order.products.all())

    context = {
        'customer': customer,
        'products_week': products_week,
        'products_month': products_month,
        'products_year': products_year,
    }

    return render(request, 'orders/ordered_products_sort.html', context)


# более универсальная функция, задаём количество дней произвольно
def fetch_ordered_products_by_days(request, customer_id, num_days):
    customer = get_object_or_404(Customer, pk=customer_id)
    today = timezone.now().date()
    start_date = today - timedelta(days=num_days)
    orders = Order.objects.filter(customer=customer, order_date__gte=start_date)

    products = set()

    for order in orders:
        products.update(order.products.all())

    context = {
        'customer': customer,
        'products': products,
        'num_days': num_days,
    }
    return render(request, 'orders/ordered_products_sort.html', context)


# TODO Дописать реализацию
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            form.save_m2m()
            return redirect('add_customer_products', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})


def add_customer_products(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save_m2m()
            form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/add_customer_products.html', {'form': form, 'order': order})
