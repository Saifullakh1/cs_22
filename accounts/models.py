from django.db import models
from django.contrib.auth.hashers import make_password


class GenderChoice(models.Choices):
    male = 'male'
    female = 'female'


class Account(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    age = models.IntegerField(default=0, verbose_name="Возраст")
    email = models.EmailField(blank=True, unique=True, verbose_name="Почта")
    avatar = models.FileField(upload_to="avatar", blank=True, verbose_name="Аватар")
    password = models.CharField(max_length=50, blank=True, verbose_name="Пароль")
    username = models.CharField(max_length=50, unique=True, blank=True, verbose_name="Имя пользователя")
    gender = models.CharField(max_length=10, choices=GenderChoice.choices, verbose_name="Пол")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"


