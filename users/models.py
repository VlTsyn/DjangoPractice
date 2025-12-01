from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    first_name = models.CharField(max_length=35, verbose_name='Имя', blank=True, null=True, help_text='Введите имя')
    last_name = models.CharField(max_length=35, verbose_name='Фамилия', blank=True, null=True, help_text='Введите фамилию')
    phone = models.CharField(max_length=15, verbose_name='Телефон', blank=True, null=True, help_text='Введите номер телефона')
    avatar = models.ImageField(upload_to='avatars/',verbose_name='Аватар', blank=True, null=True, help_text='Загрузите фото профиля')
    country = models.CharField(max_length=35, verbose_name='Страна', blank=True, null=True, help_text='Ваша страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

