from django.db import models


class Swiped(models.Model):
    '''滑动记录'''
    FALGS = (
        ('superlike', '上滑'),
        ('like', '右滑'),
        ('dislike', '左滑'),

    )
    uid = models.IntegerField(verbose_name='滑动者的 UID')
    sid = models.IntegerField(verbose_name='被滑动者的 UID')
    flag = models.CharField(max_length=10, choices=FALGS)
    dtime = models.DateTimeField(auto_now=True)


class Friend(models.Model):
    '''好友关系'''
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()
