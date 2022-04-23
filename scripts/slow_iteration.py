from performances import tasks


def run(*args):
    num = 50
    if 'num' in args:
        num = int(args[1])
    tasks.daily_performance_task.delay(num)

