from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import DO_NOTHING
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Cleaner(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя')
    surname = models.CharField(max_length=127, verbose_name='Фамилия')
    description = models.TextField(blank=True, verbose_name='Описание')

    
    class Meta:
        verbose_name = 'Уборщица'
        verbose_name_plural = 'Уборщицы'

    def __str__(self) -> str:
        return f'Уборщица "{self.name}"'

class TypeOfNumber(models.Model):
    type_of_number = models.CharField(max_length=127, verbose_name='Тип Номера')

    class Meta:
        verbose_name = 'Тип Номера'
        verbose_name_plural = 'Типы Номеров'

    def __str__(self) -> str:
       return f'"{self.type_of_number}"'

class Room(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название Номера')
    number = models.IntegerField(verbose_name='Номер комнаты')
    about = models.TextField(blank = True, verbose_name='Описание номера')
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/", verbose_name='Фото')
    type_of_number = models.ForeignKey(TypeOfNumber, on_delete=DO_NOTHING, verbose_name='Тип номера')
    rent_pay = models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Стоимость за ночь' )
    cleaner = models.ForeignKey(Cleaner, on_delete=DO_NOTHING, verbose_name='Уборщица')

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self) -> str:
        return f'Комната"{self.number}"'

class Order(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Комната', blank=True)
    visitor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Посетитель', blank=True, null=True)
    start_date = models.DateField(verbose_name='Дата вьезда')
    date_of_daparture = models.DateField(verbose_name='Дата выезда')
    total_cost = models.IntegerField(verbose_name='Суммарна стоимость', blank=True, null=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self) -> str:
        return f'Бронь "{self.room}"'

