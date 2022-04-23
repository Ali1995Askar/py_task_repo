import time

from celery.utils.log import get_task_logger
from django.db.models import F, Q
from celery import shared_task
from performances import models

logger = get_task_logger(__name__)


@shared_task(ignore_result=True)
def daily_performance_task(num: int):
    logger.info('daily_performance_task running now')
    objs = models.DailyPerformance.objects.filter(
        (~Q(cost=0)) & (Q(revenue__gt=2 * F('cost')) | Q(revenue__gt=1000))
    )[:num]

    for obj in objs.iterator():
        logger.info('Before Sleep !!!!!!!!!!')
        time.sleep(60)
        logger.info(obj)
        logger.info('After Sleep !!!!!!!!!!')

    logger.info('daily_performance_task done.')
