from django.db import models

# Create your models here.


class Newspost(models.Model):
    title = models.CharField('Заголовок новости', max_length=200)
    short_description = models.CharField('Краткое описание', max_length=200)
    text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    # def __str__(self):
    #     return self.title
