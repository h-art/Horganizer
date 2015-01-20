from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Period(models.Model):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    comment = models.CharField(null=True, blank=True, max_length=255)
    job = models.ForeignKey('Job')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.start_date.strftime('%d/%m/%Y') + ' - ' + self.end_date.strftime('%d/%m/%Y')

class Job(models.Model):
    title = models.CharField(null=False, blank=False, max_length=50)

    def __unicode__(self):
        return self.title

class Employee(models.Model):
    user = models.OneToOneField(User)
    role = models.ForeignKey('Role')

class Role(models.Model):
    title = models.CharField(null=False, blank=False, max_length=20)

    def __unicode__(self):
        return self.title
