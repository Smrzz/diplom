from django.db import models

class New(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание', blank=True, null=True)
    cover_image = models.ImageField('Изображение', upload_to='news_covers/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'