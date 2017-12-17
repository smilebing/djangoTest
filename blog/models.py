from django.db import models
from django.utils import timezone

# Create your models here.

class  BlogDetail(models.Model):
    def __str__(self):
        return self.title

    title=models.TextField()
    content=models.TextField()
    createTime=models.DateTimeField('create time')
    updateTime=models.DateTimeField('update time',blank=True,null=True)
    author=models.CharField(max_length=200)


class Article(models.Model):
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=100,blank=True)
    date_time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.title

    class Mate:
        ordering=['-date_time']