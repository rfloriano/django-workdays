import datetime
import workdays

from django.db import models

from holidays.models import Holiday


class Quarter(models.Model):
    name = models.CharField('name', max_length=50)
    start = models.DateField()
    end = models.DateField()

    class Meta:
        verbose_name = "Quarter"
        verbose_name_plural = "Quarter"

    def __unicode__(self):
        return self.name

    @classmethod
    def get_current_quarters(cls, *args, **kwargs):
        now = datetime.datetime.now()
        return Quarter.objects.filter(start__lte=now, end__gte=now, *args, **kwargs)

    def goals(self):
        return Goal.objects.filter(quarter=self)

    def remaining_days(self):
        holidays = Holiday.objects.filter(start__gte=self.start, end__lte=self.end)
        range_ = []
        for holiday in holidays:
            range_ += holiday.get_individual_dates()
        return workdays.networkdays(datetime.date.today(), self.end, range_)

    def to_dict(self):
        return {
            'name': self.name,
            'start': self.start.strftime('%Y/%m/%d'),
            'end': self.end.strftime('%Y/%m/%d'),
            'goals': [goal.to_dict() for goal in self.goals()],
            'remaining_days': self.remaining_days(),
        }


class Goal(models.Model):
    name = models.CharField('name', max_length=100)
    quarter = models.ForeignKey(Quarter)
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Goal"
        verbose_name_plural = "Goals"

    def __unicode__(self):
        return self.name

    def to_dict(self):
        return {
            'name': self.name,
            'quarter': self.quarter.name,
            'is_done': self.is_done,
        }
