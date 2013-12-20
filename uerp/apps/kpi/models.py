from django.db import models


class Period(models.Model):
    calendar = models.CharField('Календарь', max_length=3)
    month = models.IntegerField('Месяц')
    year = models.IntegerField('Год')
    days = models.IntegerField('Рабочие дни')

    def __str__(self):
        return '{year}/{month}'.format(year=self.year, month=self.month)

    class Meta:
        db_table = 'kpi_period'


class Indicators:
    name = models.CharField('Название показателя', max_length=255)
    units = models.CharField('Единицы измерения', max_length=50)
    formula = models.TextField('Формула расчета')


    class Meta:
        db_table = 'kpi_indicators_reference'