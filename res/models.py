from django.db import models


class Department(models.Model):
    name = models.CharField('Название', max_length=128)
    parent = models.ForeignKey('self', verbose_name='Родительское направление')
    department_time = models.CharField('Рабочее время', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hr_department'


class Job(models.Model):
    name = models.CharField('Название', max_length=128)
    department = models.ForeignKey('Department', verbose_name='Направление')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hr_job'


class Resource(models.Model):
    name = models.CharField('Название', max_length=128)
    active = models.BooleanField('Активен')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resource_resource'


class Employee(models.Model):
    job = models.ForeignKey('Job', verbose_name='Должность')
    department = models.ForeignKey('Department', verbose_name='Направление')
    resource = models.ForeignKey('Resource', verbose_name='Ресурс')
    mobile_phone = models.CharField('Мобильный телефон', max_length=32)
    work_phone = models.CharField('Рабочий телефон', max_length=32)
    work_email = models.CharField('Рабочий email', max_length=240)

    def __str__(self):
        return self.resource.name

    class Meta:
        db_table = 'hr_employee'