from django.db import models


class Partner(models.Model):
    name = models.CharField('Партнер (основной сайт)', max_length=250)
    ur_name = models.CharField('Юридическое название компании', max_length=250)

    def __unicode__(self):
        partner = ''
        if self.ur_name:
            partner += self.ur_name
        if self.name:
            partner += ' ({})'.format(self.name,)
        return partner

    class Meta:
        db_table = 'res_partner'