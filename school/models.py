from django.db import models


class Teacher(models.Model):
    owner = models.ForeignKey('Accounts.CustomUser',
                              related_name='teachers')

    name = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Teacher, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']


class Student(models.Model):
    name = models.CharField(max_length=40, unique=True)
    GPA = models.FloatField()
    teacher = models.ForeignKey('Teacher')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name', 'GPA']
# Create your models here.
