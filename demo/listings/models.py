from django.db import models
from datetime import datetime
from realtors.models import Realtor


class State(models.Model):
    state = models.CharField(max_length=50, unique=True, verbose_name='Район')

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return self.state


class District(models.Model):
    district = models.CharField(max_length=50, unique=True, verbose_name='МикроРайон')

    class Meta:
        verbose_name = 'МикроРайон'
        verbose_name_plural = 'МикроРайоны'

    def __str__(self):
        return self.district


class Bedrooms(models.Model):
    bedrooms = models.CharField(max_length=50, unique=True, verbose_name='Катигории квартир')

    class Meta:
        verbose_name = 'Катигории квартир'
        verbose_name_plural = 'Катигории квартир'

    def __str__(self):
        return self.bedrooms


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, verbose_name='Риелтор')
    title = models.CharField(max_length=50, verbose_name='Улица')
    # city = models.CharField(max_length=100)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(default=datetime.now, verbose_name='Дата регистрации')
    # updated_at = models.DateTimeField(default=datetime.now, verbose_name='Дата Обновления')
    list_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Время')
    bedrooms = models.ForeignKey(Bedrooms, on_delete=models.DO_NOTHING, verbose_name='Квартиры')
    # state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, verbose_name='Район')
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, verbose_name='МикроРайон')
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, default=0.00, verbose_name='цена')
    old_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Старая цена')
    House_number = models.IntegerField(blank=True, verbose_name='Номер дома')
    entrance_number = models.IntegerField(blank=True, verbose_name='Номер подьезда')
    apartment_number = models.IntegerField(blank=True, verbose_name='Номер квартиры')
    total_floors = models.IntegerField(blank=True, verbose_name='Этажей в доме')
    floor = models.IntegerField(blank=True, verbose_name='Этаж')
    flat_area = models.IntegerField(blank=True, verbose_name='Общая площадь')
    kitchen_area = models.IntegerField(blank=True, verbose_name='Площадь кухни')
    description = models.TextField(blank=True, verbose_name='Описание квартиры')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.FileField(upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'

    # is_active = models.BooleanField(default=True)

    #     address = models.CharField(max_length=200)

    # zipcode = models.CharField(max_length=20)
    # price = models.IntegerField()
    # bedrooms = models.IntegerField()
    # bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    # garage = models.IntegerField(default=0)
    # sqft = models.IntegerField()
    # lot_size = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return self.title
