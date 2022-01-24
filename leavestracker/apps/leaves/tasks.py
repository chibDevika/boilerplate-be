from celery.decorators import task
from leavestracker.apps.leaves.models import Leaves

#This task is used to send notification to the Slack channel every morning which contains a list of people who will be AFK that day.
@task
def afk_employees():
    Leaves.notify_on_slack_absent_employees()
