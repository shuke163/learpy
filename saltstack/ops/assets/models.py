from django.db import models


# Create your models here.
class HostGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name='主机组名')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('name',)


class Host(models.Model):
    OFFLINE = 0
    ONLINE = 1
    SALT_STATUS = (
        (OFFLINE, 'OFFLINE'),
        (ONLINE, 'ONLINE'),
    )
    id = models.AutoField(primary_key=True)
    hostGroup = models.ForeignKey(HostGroup, null=False, on_delete=models.PROTECT, verbose_name='主机组')
    serialNumber = models.CharField(max_length=80, null=False, blank=False, unique=True, verbose_name='系列号')
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name='内网IP')
    ipEth1 = models.GenericIPAddressField(null=True, blank=True, verbose_name='外网IP')
    kernel = models.CharField(max_length=60, null=True, blank=True, verbose_name='内核')
    os = models.CharField(max_length=60, null=True, blank=True, verbose_name='操作系统')
    osArch = models.CharField(max_length=60, null=True, blank=True, verbose_name='系统架构')
    osRelease = models.CharField(max_length=60, null=True, blank=True, verbose_name='系统版本')
    saltId = models.CharField(max_length=60, null=True, blank=True, verbose_name='salt minion id')
    saltStatus = models.IntegerField(choices=SALT_STATUS, null=False, default=OFFLINE, verbose_name='salt状态')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updateTime = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')

    class Meta:
        ordering = ('hostGroup__name', 'saltId', '-id')
