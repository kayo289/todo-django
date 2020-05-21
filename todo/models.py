from django.db import models

# Create your models here.
# 継承しているらしい
class TodoModel(models.Model):
    title = models.CharField(max_length = 100)
    memo = models.TextField()
    # 特殊メソッド
    def __str__(self):
        return self.title