from django.db import models
from django.contrib.auth.models import User


class FeedbackModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Отзыв')
    count_like = models.IntegerField(default=0, null=True)
    estimation = models.IntegerField(verbose_name='Оценка', null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user,} Отзыв: {self.content}'

