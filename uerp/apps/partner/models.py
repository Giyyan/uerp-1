from django.db import models


class Partner(models.Model):
    name = models.CharField('Партнер (основной сайт)', max_length=250)
    ur_name = models.CharField('Юридическое название компании', max_length=250)

    class Meta:
        db_table = 'res_partner'