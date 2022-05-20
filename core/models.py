from django.db import models
from datetime import datetime

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    # Test

    def __str__(self):
        return self.name


class Employee(models.Model):

    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    dni = models.CharField(max_length=10,unique=True)
    date_joined = models.DateField(default=datetime.now)
    date_create = models.DateTimeField(auto_now=True)
    age = models.PositiveSmallIntegerField(default=0)
    salary = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cVitae = models.FileField(upload_to='cVitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleados'
        ordering = ['id']
