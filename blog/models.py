from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import *

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=100)#标题
    body=models.TextField()#正文
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()#最后修改时间
    excerpt=models.CharField(max_length=200,blank=True)#摘要
    category=models.ForeignKey(Category,on_delete=models.CASCADE,)
    tags=models.ManyToManyField(Tag,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])