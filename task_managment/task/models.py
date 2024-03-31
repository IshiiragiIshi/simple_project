from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=40)
    text = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
