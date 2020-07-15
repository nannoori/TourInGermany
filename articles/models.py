from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank = True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # add later
    # add later
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50] + '...'

#Models.py
class Comment(models.Model):
    articles = models.ForeignKey(Article, related_name = 'Comments',on_delete=models.CASCADE)
    user = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()
    def __str__(self):
        return self.user
