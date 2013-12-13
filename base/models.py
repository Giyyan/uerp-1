from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')
    order = models.IntegerField(default=0)

    class MPTTMeta:
        order_insertion_by = ['order']

    def __str__(self):
        return self.name