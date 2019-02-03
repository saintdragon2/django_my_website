from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=True)

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)


