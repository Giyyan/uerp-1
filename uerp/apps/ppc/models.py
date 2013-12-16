from django.db import models
from uerp.apps.res.models import User


class ProcessLaunch(models.Model):
    partner_id = models.IntegerField('Партнер')
    service_id = models.IntegerField('Услуга')
    process_model = models.CharField('Модель', max_length=64)

    def __str__(self):
        return self.process_model

    class Meta:
        db_table = 'process_launch'


class ProcessPPC(models.Model):
    launch = models.ForeignKey('ProcessLaunch', verbose_name='Карточка запуска')
    campaign = models.CharField('Кампания', max_length=200)
    site_url = models.CharField('Сайт', max_length=255)
    date_start = models.DateField('Дата запуска кампании')
    state = models.TextField('Статус')

    def __str__(self):
        return self.site_url

    class Meta:
        db_table = 'process_ppc'


class ProcessPPCFact(models.Model):
    ppc = models.ForeignKey('ProcessPPC', verbose_name='PPC')
    campaign = models.CharField('Кампания', max_length=100)
    cash = models.FloatField('Факт')
    date = models.DateField('Дата')

    def __str__(self):
        return self.campaign

    class Meta:
        db_table = 'report_day_ppc_statistic'


class ProcessPPCDayReport(models.Model):
    partner_id = models.IntegerField('Партнер')
    service_id = models.IntegerField('Услуга')
    specialist = models.ForeignKey('User', verbose_name='Аккаунт-менеджер')
    domain_zone = models.TextField('Доменная зона')
    campaign = models.CharField('Кампания', max_length=200)
    cash = models.FloatField('Факт')
    date = models.DateField('Дата')

    class Meta:
        db_table = 'report_day_ppc'