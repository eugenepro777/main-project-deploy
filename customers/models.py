from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя клиента')
    email = models.EmailField(verbose_name='Почтовый адрес')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    address = models.TextField(verbose_name='Адрес')
    registration_date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
