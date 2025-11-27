from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='images/',blank=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    publication = models.BooleanField(default=True, verbose_name='Состояние публикации')
    views_count = models.IntegerField(default=0 ,verbose_name='Просмотры')

    def __str__(self):
        return f'{self.title} {"Опубликовано" if self.publication else "Не опубликовано"}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ['-views_count',]
