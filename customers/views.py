from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomerForm
from .models import Customer


def fetch_customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})


def fetch_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            customer = Customer(
                name=name,
                email=email,
                phone_number=phone_number,
                address=address
            )
            customer.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
        message = 'Заполните форму!'
    return render(request, 'customers/add_customer.html', {'form': form, 'message': message})


def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer.name = form.cleaned_data['name']
            customer.email = form.cleaned_data['email']
            customer.phone_number = form.cleaned_data['phone_number']
            customer.address = form.cleaned_data['address']
            customer.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(initial={
            'name': customer.name,
            'email': customer.email,
            'phone_number': customer.phone_number,
            'address': customer.address
        })
    return render(request, 'customers/edit_customer.html', {'form': form, 'customer': customer})
