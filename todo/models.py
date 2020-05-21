from django.db import models

# Create your models here.
# 継承しているらしい

PRIORITY = (('danger','heigh'),('info','normal'),('success','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length = 100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateField()
    # 特殊メソッド
    def __str__(self):
        return self.title