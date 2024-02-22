from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product


# здесь действие 'Обнулить товарный остаток' идет отдельной задекорированной функцией, modeladmin - обязательно!
@admin.action(description="Обнулить товарный остаток")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Для списка товаров"""
    list_display = ['name', 'price', 'quantity']
    list_filter = ['added_date', 'price']
    readonly_fields = ['added_date', 'preview']
    search_fields = ['description']
    search_help_text = 'Поиск товара по описанию'
    actions = [reset_quantity]
    """Для отдельного товара"""
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            }
        ),
        (
            'Отдел закупок',
            {
                'fields': ['quantity', 'price'],
                'description': 'Для управления товарными запасами'
            },
        ),
        (
            'Описание товара',
            {
                'classes': ['collapse'],
                'description': 'Подробная информация о товаре',
                'fields': ['description'],
            }
        ),
        (
            'Загрузка изображения',
            {
                'description': 'Добавьте изображение товара',
                'fields': ['image'],
            }
        ),
        (
            'Изображение товара',
            {
                'fields': ['preview'],
            }
        ),
        (
            'Прочее',
            {
                'description': 'Дата добавления',
                'fields': ['added_date'],
            }
        ),
    ]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width: 200px; height: auto;" alt="Изображения нет">')
