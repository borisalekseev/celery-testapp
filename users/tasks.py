import time

from celery import shared_task
from users.models import SomeData


@shared_task
def large_job():
    print("started large 5 seconds job")
    time.sleep(5)
    SomeData.objects.create(name="Job executed")
    print("finished large job")
