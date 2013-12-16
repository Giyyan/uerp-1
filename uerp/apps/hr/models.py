from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class Resource(models.Model):
    name = models.CharField('Название', max_length=128)
    active = models.BooleanField('Активен')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resource_resource'


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


class EmployeeManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            msg = "У сотрудника должен быть email."
            raise ValueError(msg)

        user = self.model(work_email=EmployeeManager.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser):
    job = models.ForeignKey('Job', verbose_name='Должность')
    department = models.ForeignKey('Department', verbose_name='Направление')
    resource = models.ForeignKey('Resource', verbose_name='Ресурс')
    mobile_phone = models.CharField('Мобильный телефон', max_length=32)
    work_phone = models.CharField('Рабочий телефон', max_length=32)
    work_email = models.CharField('Рабочий email', max_length=240)

    USERNAME_FIELD = "work_email"

    objects = EmployeeManager()

    def __str__(self):
        return self.resource.name

    class Meta:
        db_table = 'hr_employee'
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def get_full_name(self):
        return self.resource.name

    def get_short_name(self):
        return self.work_email