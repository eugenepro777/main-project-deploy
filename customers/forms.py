from django import forms
from .models import Customer


class CustomerForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)

    def save(self):
        cleaned_data = self.cleaned_data
        customer = Customer.objects.create(
            name=cleaned_data['name'],
            email=cleaned_data['email'],
            phone_number=cleaned_data['phone_number'],
            address=cleaned_data['address']
        )
        return customer
