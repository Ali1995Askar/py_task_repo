from django.contrib import admin
from . import models


# Register your models here.

# admin.site.register(models.Performance)

class CustomHourlyPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        'cost',
        'revenue',
        'profit',
        'datetime',
        'created_at'
    )


class CustomDailyPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        'cost',
        'revenue',
        'profit',
        'date',
        'created_at'
    )


admin.site.register(models.HourlyPerformance, CustomHourlyPerformanceAdmin)
admin.site.register(models.DailyPerformance, CustomDailyPerformanceAdmin)
