from django.db import models
# Create your models here.
#图书类
from django.utils import timezone


class Book(models.Model):
    book_id = models.BigAutoField(primary_key=True)#图书编号
    book_name = models.CharField(max_length=30)#图书名字
    book_publisher = models.CharField(max_length=30)#出版社
    book_img = models.ImageField(upload_to='img',null=True)
    book_count = models.BigIntegerField()#数量

#用户类
class User(models.Model):
    uno = models.CharField(max_length=10,primary_key=True)#用户编号
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    max_num = models.BigIntegerField(default=10)#最大借阅量
    lend_num = models.BigIntegerField(default=0)#已借阅数

    def __unicode__(self):
        return self.uname,self.lend_num,self.max_num

#借阅历史
class Lend(models.Model):
    uname = models.CharField(max_length=255)
    lbookid = models.BigIntegerField(primary_key=True)
    lbook = models.CharField(max_length=255)
    ltime = models.DateField(default = timezone.now)#借阅时间
    lpublisher = models.CharField(max_length=255)

#归还历史
class Back(models.Model):
    bid = models.BigAutoField(primary_key=True)
    uname = models.CharField(max_length=255)
    bbookid = models.BigIntegerField()
    bbook = models.CharField(max_length=255)
    btime = models.DateField(default = timezone.now)#借阅时间
    bpublisher = models.CharField(max_length=255)
