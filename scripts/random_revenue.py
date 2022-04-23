from performances import models
from django.db.models import F
from django.db.models.functions import Round
import random


def run():
    saved_daily_revenues_qs = models.DailyPerformance.objects.filter_by_min_roi(0.5)
    records_count = saved_daily_revenues_qs.count()

    print(records_count)
    print(2 * records_count)

    for idx, daily_revenue in enumerate(saved_daily_revenues_qs.iterator(), 1):
        print(f"{idx}/{records_count}")
        daily_revenue.revenue = Round(F("revenue") * random.uniform(0.5, 2), 2)
        daily_revenue.save(update_fields=['revenue', 'profit'])
