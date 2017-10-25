from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


class Category(models.Model):#创建分类
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):#创建标签
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):#创建文章数据库
    title = models.CharField(max_length=70)#标题
    body = models.TextField()#正文

    created_time = models.DateTimeField()#创建时间
    modified_time = models.DateTimeField()#修改时间

    excerpt = models.CharField(max_length=200,blank= True)#创建摘要

    category =models.ForeignKey(Category)#一对多的关联
    tags=models.ManyToManyField(Tag,blank=True)#多对多的关联

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time']

    author = models.ForeignKey(User)#设定作者








 #create your models here.
