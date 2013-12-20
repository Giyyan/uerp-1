from django.contrib.auth.models import Group
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from uerp.settings.common import AUTH_USER_MODEL


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')
    order = models.IntegerField(default=0)
    groups = models.ManyToManyField(Group, verbose_name='Группы', blank=True, related_name='g+')
    users = models.ManyToManyField(AUTH_USER_MODEL, verbose_name='Сотрудники', blank=True, related_name='u+')

    class MPTTMeta:
        order_insertion_by = ['order']

    class Meta:
        verbose_name = 'Меню'

    def __str__(self):
        return self.name