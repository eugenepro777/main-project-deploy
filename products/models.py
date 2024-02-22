from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    added_date = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    image = models.ImageField(upload_to='images/', default='default_image.png', blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
