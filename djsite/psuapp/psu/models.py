from django.db import models

# Create your models here.


class Problem(models.Model):
    naming = models.CharField(max_length=50, verbose_name = "Наименование возможной проблемы")
    description= models.CharField(max_length = 255, verbose_name = "Описание возможной проблемы")
    icon = models.ImageField(blank=True, null = True, upload_to='images', verbose_name="Изображение")

    def __str__(self) :
        return self.naming

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("problem", kwargs={"pr_id": self.pk})
    
    class Meta:
        verbose_name = "Возможная проблема"
        verbose_name_plural = "Возможные проблемы"


class FAQ(models.Model):
    section_id = models.ForeignKey(Problem, blank = True, null = True,on_delete=models.SET_NULL)
    question = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse("faq_detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ['section']
        verbose_name = "Часто задаваемый вопрос"
        verbose_name_plural = "Часто задаваемые выопросы"


