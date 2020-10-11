from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


#class Comment(models.Model):
    #post = models.ForeignKey(NeedPost, on_delete=models.CASCADE)
    #text = models.TextField(max_length=500)
    #date_posted = models.DateTimeField(default=timezone.now)
    #name = models.CharField(max_length=250)

    #def __str__(self):
        #return self.text


class HaveToilet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/')
    description = models.TextField(max_length=500)
