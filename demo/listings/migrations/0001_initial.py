# Generated by Django 2.1.7 on 2019-03-31 15:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bedrooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrooms', models.CharField(max_length=50, unique=True, verbose_name='Катигории квартир')),
            ],
            options={
                'verbose_name': 'Катигории квартир',
                'verbose_name_plural': 'Катигории квартир',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50, unique=True, verbose_name='МикроРайон')),
            ],
            options={
                'verbose_name': 'МикроРайон',
                'verbose_name_plural': 'МикроРайоны',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Улица')),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Время')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, verbose_name='цена')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Старая цена')),
                ('House_number', models.IntegerField(blank=True, verbose_name='Номер дома')),
                ('entrance_number', models.IntegerField(blank=True, verbose_name='Номер подьезда')),
                ('apartment_number', models.IntegerField(blank=True, verbose_name='Номер квартиры')),
                ('total_floors', models.IntegerField(blank=True, verbose_name='Этажей в доме')),
                ('floor', models.IntegerField(blank=True, verbose_name='Этаж')),
                ('flat_area', models.IntegerField(blank=True, verbose_name='Общая площадь')),
                ('kitchen_area', models.IntegerField(blank=True, verbose_name='Площадь кухни')),
                ('description', models.TextField(blank=True, verbose_name='Описание квартиры')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.FileField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('bedrooms', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Bedrooms', verbose_name='Квартиры')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.District', verbose_name='МикроРайон')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor', verbose_name='Риелтор')),
            ],
            options={
                'verbose_name': 'Обьявление',
                'verbose_name_plural': 'Обьявления',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50, unique=True, verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.State', verbose_name='Район'),
        ),
    ]
