from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class NeedPost(models.Model):
    name = models.CharField(max_length=250)
    choices = (
        (0, 'I can hold it in'),
        (1, 'I kinda have to go now'),
        (2, 'I GOTTA SHIT'),
    )
    priority = models.IntegerField(null=True,
                                   choices=choices,
                                   default=choices[0][0],)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(NeedPost, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.text


class HaveToilet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.TextField(max_length=500)
