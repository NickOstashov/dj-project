from django.db import models

# Create your models here.


class Problem(models.Model):
    naming = models.CharField(max_length=50, verbose_name = "Наименование возможной проблемы")
    description= models.CharField(max_length = 255, verbose_name = "Описание возможной проблемы")
    icon = models.ImageField(blank=True, null = True, upload_to='images', verbose_name="Изображение")

    def __str__(self):
        return self.naming
    
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = "Возможная проблема"
        verbose_name_plural = "Возможные проблемы"

