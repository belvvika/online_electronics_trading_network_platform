from django.db import models

class Supplier(models.Model):
    LEVELS = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(
        max_length=100,
        verbose_name='Поставщик',
        help_text='Название поставщика'
    )
    email = models.EmailField(
        max_length=100,
        verbose_name='Электронная почта',
        help_text='Адрес электронной почты поставщика'
    )
    country = models.CharField(
        max_length=100,
        verbose_name='Страна',
        help_text='Страна поставщика'
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Город',
        help_text='Город поставщика'
    )
    street = models.CharField(
        max_length=100,
        verbose_name='Улица',
        help_text='Улица поставщика'
    )
    house_number = models.CharField(
        max_length=100,
        verbose_name='Номер дома',
        help_text='Номер дома поставщика'
    )
    level = models.ImageField(
        choices=LEVELS,
        verbose_name='Уровень поставщика',
        help_text='Уровень поставщика'
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Долг',
        help_text='Долг поставщика'
    )
    create_time = models.DateTimeField(
        verbose_name='Дата создания',
        help_text='Дата создания поставщика'
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название продукта',
        help_text='Название продукта'
    )
    model = models.CharField(
        max_length=100,
        verbose_name='Модель',
        help_text='Модель продукта'
    )
    date_release = models.DateField(
        verbose_name='Дата выпуска',
        help_text='Дата выпуска продукта'
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name='Поставщик',
        help_text='Поставщик продукта'
    )

    def __str__(self):
        return f'{self.name} ({self.model})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
