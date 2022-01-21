import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leavestracker.settings.local")

app = Celery("leavestracker", broker_url="amqp://guest:**@127.0.0.1:5672//:")
task = app.task

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    "notification_scheduler": {
        "task": "leavestracker.apps.leaves.tasks.afk_employees",
        "schedule": 15, #crontab(hour=9, minute=0),
    }
}
