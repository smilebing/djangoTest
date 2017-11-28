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