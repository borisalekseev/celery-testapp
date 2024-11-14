import time

from celery import Celery


app = Celery('celery_large_job_app', broker='redis://redis:6379')


@app.task
def large_job():
    print("started large 5 seconds job")
    time.sleep(5)
    print("finished large job")
