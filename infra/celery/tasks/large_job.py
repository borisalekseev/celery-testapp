import time

from celery import shared_task
from simple_tasks_app.models import SomeData


@shared_task(bind=True)
def large_job(self):
    print("started large 5 seconds job")
    print(type(self))
    print(self.request)
    time.sleep(5)
    SomeData.objects.create(name="Job %s executed" % self)
    print("finished large job")
