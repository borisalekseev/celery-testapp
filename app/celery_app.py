import os

from celery import Celery
from kombu import Exchange, Queue

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery('celery_large_job_app', broker='redis://redis:6379')
app.config_from_object(f"django.conf:settings")

large_job_exchange = Exchange('large_job', type='direct')
quick_tasks_exchange = Exchange('quick_tasks', type='direct')

app.conf.task_queues = (
    Queue('large_job', large_job_exchange, routing_key='large_job'),
    Queue('quick_tasks', quick_tasks_exchange, routing_key='quick_tasks')
)
app.conf.task_default_queue = 'quick_tasks'
app.conf.task_default_exchange = 'quick_tasks'
app.conf.task_default_routing_key = 'quick_tasks'
app.conf.task_routes = {
    'infra.celery.tasks.large_job.large_job': {
        'queue': 'large_job',
        'exchange': 'large_job'
    }
}


app.autodiscover_tasks(
    related_name="large_job"
)
