import time

from infra.celery.tasks.large_job import large_job
from infra.celery.tasks.quick_tasks import quick_task
from django.http import HttpResponse

from app.celery_app import app


def run_large_task(request):
    large_job.delay()
    return HttpResponse("Ok!")


def check_running(request):
    current_tasks = app.control.inspect().active()
    return HttpResponse(str(current_tasks))


def run_quick_task(request):
    metadata = quick_task.delay()
    print(metadata)
    return HttpResponse("Ok!")
