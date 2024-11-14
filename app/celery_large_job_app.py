import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery('celery_large_job_app', broker='redis://redis:6379')
app.config_from_object(f"django.conf:settings")
app.autodiscover_tasks()
