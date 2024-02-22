import csv
from django.contrib import admin
from django.http import HttpResponse
from django.db import models

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['display_id', 'customer', 'total_amount', 'order_date']
    list_filter = ['customer', 'order_date', 'products']
    search_fields = ['customer__name']
    search_help_text = 'Поиск заказа по клиенту'
    readonly_fields = ['order_date']
    actions = ['export_to_csv']
    fieldsets = [
        ('Основная информация', {
            'fields': ['customer', 'total_amount', 'order_date']
        }),
        ('Товары', {
            'fields': ('products',)
        })
    ]
    filter_horizontal = ('products',)

    def save_model(self, request, obj, form, change):
        if not obj.total_amount:
            obj.total_amount = obj.products.aggregate(total=models.Sum('price'))['total']
        super().save_model(request, obj, form, change)
        obj.products.set(form.cleaned_data['products'])
        obj.save()
        # obj.products.set(form.cleaned_data['products'])

    def display_id(self, obj):
        return f"Заказ №{obj.id}"
    display_id.short_description = 'Номер заказа'

    # здесь встраиваем действие 'Экспорт в CSV' внутрь класса, как его метод, modeladmin не нужен
    @admin.action(description='Экспорт в CSV')
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Клиент', 'Сумма заказа', 'Дата заказа'])

        for order in queryset:
            writer.writerow([order.id, order.customer.name, order.total_amount, order.order_date])
        return response
