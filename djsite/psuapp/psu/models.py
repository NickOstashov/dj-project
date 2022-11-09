from django.db import models

# Create your models here.


class Problem(models.Model):
    '''
    Содержимое главной страницы 

    Поля модели:
    [*]naming - наименование возможной проблемы (50 символа максимум)
    [*]description - описание проблемы (255 символа максимум)

    '''
    naming = models.CharField(max_length=50, verbose_name = "Наименование возможной проблемы")
    description= models.CharField(max_length = 255, verbose_name = "Описание возможной проблемы")

    def __str__(self):
        return self.naming
    
    class Meta:
        verbose_name = "Возможная проблема"
        verbose_name_plural = "Возможные проблемы"

