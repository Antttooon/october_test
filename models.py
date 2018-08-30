from django.db import models
from django.db.models import Count, Max, F


class CountryQuerySet(models.QuerySet):
    def with_num_cities(self):
        return self.annotate(num_cities=Count('cities'))

    def with_biggest_city_size(self):
        return self.annotate(biggest_city_size=Max('cities__area'))


class CityQuerySet(models.QuerySet):
    def with_dencity(self):
        return self.annotate(dencity=F('area') / F('population'))


class Country(models.Model):
    name = models.CharField(
        'Название',
        max_length=255
    )

    objects = CountryQuerySet.as_manager()

    def __str__(self):
        return self.name



class City(models.Model):
    country = models.ForeignKey(
        Country,
        verbose_name='Страна',
        related_name='cities',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Название',
        max_length=255
    )
    population = models.FloatField(
        'Население'
    )
    area = models.FloatField(
        'Площадь'
    )
    objects = CityQuerySet.as_manager()

    def __str__(self):
        return self.name
