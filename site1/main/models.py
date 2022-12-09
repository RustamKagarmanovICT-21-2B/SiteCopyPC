from django.db import models


class Person(models.Model):
    phoneNumber = models.IntegerField('Номер телефона')
    name = models.CharField('ФИО', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
