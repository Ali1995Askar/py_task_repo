import datetime
import random

from django.db.models import F, Q
from django.db.models.functions import Round

from django.test import TestCase
from unittest import mock

from . import models


class TestHourlyPerformanceModel(TestCase):
    def setUp(self) -> None:
        self.test_cost_value = 100.125
        self.test_revenue_value = 180.22
        self.test_datetime_value = datetime.datetime.now()
        self.test_date_value = datetime.date.today()
        self.min_roi = 0.5
        self.number_records = 100
        self.random_value = random.uniform(0.5, 2)

    def test_create_daily_performance_with_correct_values(self):
        new_daily_performance_obj = models.DailyPerformance.objects.create(
            cost=self.test_cost_value,
            revenue=self.test_revenue_value,
            date=self.test_date_value
        )

        self.assertEqual(new_daily_performance_obj.cost,
                         self.test_cost_value)

        self.assertEqual(new_daily_performance_obj.revenue,
                         self.test_revenue_value)

        self.assertEqual(new_daily_performance_obj.date,
                         self.test_date_value)

        self.assertEqual(new_daily_performance_obj.profit,
                         self.test_revenue_value - self.test_cost_value)

    def test_create_hourly_performance_with_correct_values(self):
        new_hourly_performance_obj = models.HourlyPerformance.objects.create(
            cost=self.test_cost_value,
            revenue=self.test_revenue_value,
            datetime=self.test_datetime_value
        )

        self.assertEqual(new_hourly_performance_obj.cost,
                         self.test_cost_value)

        self.assertEqual(new_hourly_performance_obj.revenue,
                         self.test_revenue_value)

        self.assertEqual(new_hourly_performance_obj.datetime,
                         self.test_datetime_value)

        self.assertEqual(new_hourly_performance_obj.profit,
                         self.test_revenue_value - self.test_cost_value)

    def test_filter_by_min_roi_method(self):
        """
            Because task ask to save profit value i used calculated field and overwrite save method to calculate the result
            that the reason i didn't use property so i can't use bulk_create method to create objects as you know 
            bulk_create will not call save() method or send post_save or pre_save() signals
        """
        for idx in range(1, self.number_records):
            models.DailyPerformance.objects.create(
                cost=idx,
                revenue=idx,
                date=self.test_date_value
            )

        for idx in range(1, self.number_records):
            models.DailyPerformance.objects.create(
                cost=idx,
                revenue=idx + 1000,
                date=self.test_date_value
            )

        models.DailyPerformance.objects.create(
            cost=100,
            revenue=151,
            date=self.test_date_value
        )

        models.DailyPerformance.objects.create(
            cost=100,
            revenue=150,
            date=self.test_date_value
        )
        self.assertEqual(100,
                         models.DailyPerformance.objects.filter_by_min_roi(
                             self.min_roi).count())

    def test_slow_iteration_task_query(self):

        for idx in range(1, self.number_records):
            models.DailyPerformance.objects.create(
                cost=0,
                revenue=idx,
                date=self.test_date_value
            )

        for idx in range(1, self.number_records):
            models.DailyPerformance.objects.create(
                cost=idx,
                revenue=idx,
                date=self.test_date_value
            )

        for idx in range(1, self.number_records):
            models.DailyPerformance.objects.create(
                cost=idx,
                revenue=1000 + idx,
                date=self.test_date_value
            )

        for idx in range(1, self.number_records):
            models.DailyPerformance.objects.create(
                cost=idx,
                revenue=2 * idx + 1,
                date=self.test_date_value
            )

        self.assertEqual(198,
                         models.DailyPerformance.objects.filter(
                             (~Q(cost=0)) & (Q(revenue__gt=2 * F('cost')) | Q(revenue__gt=1000))
                         ).count())

    def test_set_revenue_multiplied_by_random_number(self):
        daily_revenue = models.DailyPerformance.objects.create(
            cost=100,
            revenue=200,
            date=self.test_date_value
        )

        self.assertEqual(daily_revenue.revenue, 200)
        self.assertEqual(daily_revenue.profit, 100)
        old_revenue = daily_revenue.revenue

        daily_revenue.revenue = Round(F("revenue") * self.random_value, 4)
        daily_revenue.save(update_fields=['revenue', 'profit'])
        daily_revenue.refresh_from_db()

        self.assertAlmostEqual(daily_revenue.revenue, self.random_value * old_revenue, 4)
        self.assertEqual(daily_revenue.profit, daily_revenue.revenue - daily_revenue.cost)

    @mock.patch("scripts.slow_iteration.tasks.daily_performance_task.delay")
    def test_daily_performance_task_running(self, mocked_task: mock.Mock):
        from scripts import slow_iteration
        slow_iteration.run()
        mocked_task.assert_called_once()
