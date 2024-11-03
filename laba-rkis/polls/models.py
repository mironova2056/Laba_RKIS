import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    username = models.CharField(max_length=100, verbose_name="Логин", unique=True)
    password = models.CharField(max_length=100, verbose_name="Пароль")
    avatar = models.ImageField(upload_to="polls/user", verbose_name="Фото профиля")
    email = models.EmailField(max_length=100, verbose_name="Почта", unique=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Question(models.Model):
    text = models.CharField("Вопрос",max_length=200)
    pub_date = models.DateTimeField('Дата публикации')
    short_description = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='polls/questions', blank=True)
    votes = models.IntegerField(default=0, blank=True)
    voted_by = models.ManyToManyField(User, related_name='voted_questions', blank=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=3)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField("Вариант ответа",max_length=250)
    votes = models.IntegerField("Голоса",default=0)

    def vote_percentage(self):
        if self.question.votes > 0:
            return round(self.votes * 100 / self.question.votes)
        return 0

    def __str__(self):
        return self.text