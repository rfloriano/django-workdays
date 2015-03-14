import datetime

from django.db import models


class Holiday(models.Model):
    name = models.CharField('name', max_length=50)
    start = models.DateField()
    end = models.DateField()
    is_every_year = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Holiday"
        verbose_name_plural = "Holidays"

    def __unicode__(self):
        return self.name

    def get_individual_dates(self):
        if self.start == self.end:
            return [self.start]
        dates = []
        for n in range(int((self.end - self.start).days)):
            dates.append(self.start + datetime.timedelta(n))
        return dates
