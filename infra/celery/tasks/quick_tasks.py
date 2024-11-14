import time

from celery import shared_task
from simple_tasks_app.models import SomeData


@shared_task
def quick_task():
    print("started quick 3 seconds job")
    time.sleep(3)
    SomeData.objects.create(name="Quick task")
    print("finished quick job")
