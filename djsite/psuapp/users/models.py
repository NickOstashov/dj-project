from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from psu.models import typeProblem, Problem

class CustomUser(AbstractUser):
    position = models.CharField(max_length=255, blank = True,verbose_name="Должность")

    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Applications(models.Model):
    user = models.ForeignKey('CustomUser', blank = True, null = True,on_delete=models.SET_NULL, verbose_name="Индентификатотр пользователя")
    name = models.CharField(max_length=100,blank = True, verbose_name="Имя")
    surname = models.CharField(max_length=100,blank = True, verbose_name="Фамилия")
    comment = models.TextField(blank=True,verbose_name="Комментарии")
    position = models.CharField(max_length=100,blank=True,verbose_name="должность")
    tel = PhoneNumberField(region="RU",blank = True,verbose_name = "Номер телефона")
    problem = models.ForeignKey(Problem,blank = True, null = True,on_delete=models.PROTECT, verbose_name="Вид пробдлемы")
    kind_of_problem = models.ForeignKey(typeProblem, blank = True, null = True,on_delete=models.PROTECT, verbose_name="Вариант проблемы")
    additional_info = models.JSONField(default={},blank=True,verbose_name="Дополнительная информация")
    STATUS = (
        ('SU','успешно завершена'),
        ('NW','новая заявка'),
        ('RE','заявка отклонена'),
        ('AI','требуется уточнение'),
        ('IP','в процессе выполнения'),
        ('CH','проверка')
    )

    status = models.CharField(max_length=2,
                           choices=STATUS,
                           default='NW',
                           verbose_name="Статус"
                           )

    class Meta:
        ordering = ['user_id']
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"