from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    position = models.CharField(max_length=255, blank = True,verbose_name="Должность")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        
