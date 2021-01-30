from django.db import models
from datetime import date


class Logo(models.Model):
    "logotipe of activity"
    image = models.ImageField('Logo', upload_to="logo/", default='default.png')   #default!



class Activity(models.Model):
    """ Activity """
    name = models.CharField(max_length=60, verbose_name='Activity name')
    image = models.ForeignKey(Logo, verbose_name='Logo', on_delete=models.CASCADE)  #blank + default?

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Activity name'
        verbose_name_plural = 'Activity names'


class SpendedTime(models.Model):
    """time spent for activity"""
    name = models.ForeignKey(Activity, verbose_name='Activity', on_delete=models.CASCADE)
    time = models.PositiveIntegerField(verbose_name='Elapsed time (min)')
    date = models.DateField('Date', default=date.today)

    def __str__(self):
        return f'{self.name} :{self.time} min'

    class Meta:
        verbose_name='Activity'
        verbose_name_plural = 'Activities'
