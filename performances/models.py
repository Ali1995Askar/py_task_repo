from django.db import models
from .managers import CustomDailyPerformanceManager


class Performance(models.Model):
    cost = models.FloatField(null=False)
    revenue = models.FloatField(null=False)
    profit = models.FloatField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def get_profit(self):
        result = self.revenue - self.cost
        return result

    def save(self, *args, **kwargs):
        self.profit = self.get_profit()
        super(Performance, self).save(*args, **kwargs)

    def __str__(self):
        return f'cost: {self.cost} -> revenue: {self.revenue} -> profit: {self.profit}'


class HourlyPerformance(Performance):
    datetime = models.DateTimeField()


class DailyPerformance(Performance):
    date = models.DateField()
    objects = CustomDailyPerformanceManager()
