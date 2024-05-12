from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=50, verbose_name='name')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Moto(models.Model):
    title = models.CharField(max_length=50, verbose_name='name')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'Moto'
        verbose_name_plural = 'Motos'


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, related_name='milage')
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, null=True, blank=True, related_name='milage')

    milage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.PositiveSmallIntegerField(verbose_name='год регистрации')

    def __str__(self):
        return f'{self.moto if self.moto else self.car} - {self.year}'

    class Meta:
        verbose_name = 'Пробег'
        verbose_name_plural = 'Пробег'
        ordering = ('-year',)
