from django.db import models
import datetime as dt
from django.utils import timezone


class Author(models.Model):
    author = models.CharField('Автор', max_length=200)
    password = models.IntegerField()


class Article(models.Model):
    aut = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    art_title = models.CharField('Название статьи', max_length=200)
    text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.art_title

    def was_publ(self):
        return self.pub_date >= (timezone.now() - dt.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    autor_name = models.CharField('Автор', max_length=50)
    comm_text = models.TextField('Комментарий')

    def __str__(self):
        return self.autor_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
