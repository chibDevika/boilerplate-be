from celery.decorators import task
from leavestracker.apps.leaves.models import Leaves

@task
def afk_employees():
    Leaves.notify_on_slack_absent_employees()
