from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=64)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'res_users'