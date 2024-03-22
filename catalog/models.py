from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    price = models.IntegerField(default=0, verbose_name='цена за покупку')
    photo = models.ImageField(upload_to='main/', **NULLABLE, verbose_name='изображение(превью)')
    last_change = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return f'Наименование товара: {self.name},' \
               f'Категория: {self.category}),' \
               f'Цена: {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
