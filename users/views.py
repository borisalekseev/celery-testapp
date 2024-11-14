from users.tasks import large_job
from django.http import HttpResponse


def run_large_task(request):
    large_job.delay()
    return HttpResponse("Ok!")
