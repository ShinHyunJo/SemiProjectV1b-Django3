from datetime import datetime

from django.db import models

# Create your models here.
class Member(models.Model):
    id=models.AutoField(primary_key=True)
    userid=models.CharField(max_length=18, unique=True)
    passwd=models.CharField(max_length=18)
    name=models.CharField(max_length=5)
    email=models.CharField(max_length=100)
    regdate=models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'member'          # 생성할 테이블 이름 지정
        ordering = ['-regdate']      # 정렬 기준 지정 descecnding


    def __str__(self):
        return self.userid           # 객체생성시 출력 형태 정의