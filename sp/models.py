# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink
from PIL import Image


# Create your models here.
class Address(models.Model):
    """
       Модель, що описує адресу проживання студента
    """
    country = models.CharField(max_length=100, verbose_name=u'Країна')
    city = models.CharField(max_length=100, verbose_name=u'Місто', blank=True)
    region = models.CharField(max_length=100, verbose_name=u'Область', blank=True)
    district = models.CharField(max_length=100, verbose_name=u'Район', blank=True)
    street = models.CharField(max_length=100, verbose_name=u'Вулиця')
    house_number = models.CharField(max_length=100, verbose_name=u'Номер будинку')

    class Meta:
        verbose_name = u'Адрес'
        verbose_name_plural = u'Адреси'


class StudyPlace(models.Model):
    """
       Модель, що описує місце навчання студента
    """
    name = models.TextField(max_length=500, verbose_name=u'Назва навчального закладу')
    address = models.ForeignKey(Address, verbose_name=u'Адреса')

    class Meta:
        verbose_name = u'Місце навчання'
        verbose_name_plural = u'Місця навчання'


class Student(models.Model):
    """
       Модель, що описує студента
    """
    photo = models.ImageField(verbose_name=u'Фото', upload_to='upload')
    family_name = models.CharField(max_length=100, verbose_name=u'Прізвище')
    name = models.CharField(max_length=100, verbose_name=u'Ім`я')
    father_name = models.CharField(max_length=100, verbose_name=u'По-батькові')
    squad = models.CharField(max_length=3, verbose_name=u'Взвод')
    faculty = models.CharField(max_length=100, verbose_name=u'Факультет')
    group = models.CharField(max_length=100, verbose_name=u'Група')
    specialization = models.CharField(max_length=100, verbose_name=u'Спеціальність')
    address = models.ForeignKey(Address, related_name='student_address', verbose_name=u'Місце проживання')
    birth_date = models.DateField(verbose_name=u'Дата народження')
    birth_address = models.ForeignKey(Address, related_name='student_birth_address', verbose_name=u'Місце народження')
    study_place = models.ForeignKey(StudyPlace, verbose_name=u'Навчався')
    working_place = models.TextField(max_length=500, verbose_name=u'Місце роботи')
    hobbie = models.TextField(max_length=500, verbose_name=u'Хоббі')
    contacts = models.DecimalField(max_digits=10, decimal_places=0, verbose_name=u'Номери телефонів')
    father_address = models.ForeignKey(Address, related_name='students_fathers_address', verbose_name=u'Адреса батька')
    mother_address = models.ForeignKey(Address, related_name='students_mothers_address', verbose_name=u'Адреса матері')
    father_work = models.CharField(max_length=100, verbose_name=u'Місце роботи батька')
    mother_work = models.CharField(max_length=100, verbose_name=u'Місце роботи матері')
    rb_number = models.CharField(max_length=100, verbose_name=u'Номер заліковки')
    notes = models.TextField(max_length=500, verbose_name=u'Примітки', blank=True)

    class Meta:
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенти'

    def get_absolute_url(self):
        return '/%s/%i/' % (self.squad, self.pk)

    def __unicode__(self):
        return self.family_name + ' ' + self.name + ' ' + self.father_name


class Squad(models.Model):
    """
       Модель взводу
    """
    name = models.CharField(max_length=3, verbose_name=u'Взвод')
    # student = models.ForeignKey(Student, related_name='student_squad', verbose_name=u'Студент')
    student = models.ManyToManyField(Student, related_name='student_squad', verbose_name=u'Студент')

    class Meta:
        verbose_name = u'Взвод'
        verbose_name_plural = u'Взводи'

    def get_absolute_url(self):
        return '/%s/' % self.name

    def __unicode__(self):
        return self.name


