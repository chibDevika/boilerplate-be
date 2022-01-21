import json
import requests

from leavestracker.settings.local import *

def slack_notification(message, title):
    url = "https://hooks.slack.com/services/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"
    slack_data = {
        "username": "AFK Notification",
        "icon_emoji": ":bell:",
        "channel" : "#nothing",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    headers = {'Content-Type': "application/json"}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
