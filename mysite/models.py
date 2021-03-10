from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 255)
    tags = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add = True)
    post_time = models.DateTimeField(auto_now_add = True)
    category = models.CharField(max_length = 255, default = 'uncategorized')

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args = (self.pk,))

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

RATE_CHOICES = [
    (1, '1 - Trash'),
    (2, '2 - Terrible'),
    (3, '3 - Ok'),
    (4, '4 - Good'),
    (5, '5 - Perfect'),
]

class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    text = models.TextField(max_length = 3000, blank = True)
    rate = models.PositiveSmallIntegerField(choices = RATE_CHOICES, blank = True)
    like = models.PositiveIntegerField(default = 0)
    unlike = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.user.username