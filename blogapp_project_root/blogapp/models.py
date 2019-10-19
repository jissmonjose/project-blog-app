from django.db import models
from datetime import datetime
# import the user model
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'pk': self.pk})
