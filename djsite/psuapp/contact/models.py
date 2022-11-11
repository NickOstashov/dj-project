from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30,verbose_name="Имя")
    surname = models.CharField(max_length=30,verbose_name="Фамилия")
    email = models.EmailField(max_length=254,blank=True,verbose_name="Email")
    tel = PhoneNumberField(region="RU",blank = True,verbose_name = "Номер телефона")

    # def __str__(self):
    #     return self.name

    # def __str__(self):
    #     return self.surname
    
    # def __str__(self):
    #     return self.email
    
    # def __str__(self):
    #     return self.tel

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


    
