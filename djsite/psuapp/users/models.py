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
    #user = models.ForeignKey('CustomUser', blank = True, null = True,on_delete=models.SET_NULL, verbose_name="Индентификатотр пользователя")
    user_name = models.CharField(max_length=255,blank = True, verbose_name="ФИО")
    comment = models.TextField(blank=True,verbose_name="Комментарии")
    position = models.CharField(max_length=100,blank=True,verbose_name="должность")
    tel = models.CharField(max_length=20,blank = True,verbose_name = "Номер телефона")
    kind_of_problem = models.CharField(max_length=255,blank=True,verbose_name="Наименование проблемы")
    #additional_info = models.JSONField(default={},blank=True,verbose_name="Дополнительная информация")
    # STATUS = (
    #     ('SU','успешно завершена'),
    #     ('NW','новая заявка'),
    #     ('RE','заявка отклонена'),
    #     ('AI','требуется уточнение'),
    #     ('IP','в процессе выполнения'),
    #     ('CH','проверка')
    # )

    # status = models.CharField(max_length=2,
    #                        choices=STATUS,
    #                        default='NW',
    #                        verbose_name="Статус"
    #                        )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"