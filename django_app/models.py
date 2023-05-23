from django.db import models
from django.utils import timezone

# Create your models here.
# 人物テーブルの定義


# メモテーブルの定義
class Memo(models.Model):
    memo = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Memo'
        ordering = ['id']
