import json
import requests

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
