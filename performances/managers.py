from django.db.models import F, Manager


class CustomDailyPerformanceManager(Manager):
    def filter_by_min_roi(self, min_roi: float):
        return self.annotate(roi=F('profit') / F('cost')).filter(roi__gt=min_roi)
