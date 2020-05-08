import datetime
from django.db import models

from django.utils import timezone

class futureblog(models.Model):
    blog_title = models.CharField('Название статьи', max_length = 200)
    blog_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.blog_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'



class Comment(models.Model):
    futureblog = models.ForeignKey(futureblog, on_delete = models.CASCADE)
    autor_name = models.CharField('Имя автора', max_length = 50)
    comment_text = models.CharField('Текст комментария', max_length = 200)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



