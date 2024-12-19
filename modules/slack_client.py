import os
import requests

class SlackClient:
    def __init__(self):
        self.token = os.getenv("SLACK_BOT_TOKEN")
        self.channel = os.getenv("SLACK_CHANNEL_ID")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def send_ticket_notification(self, ticket):
        """Send a Slack message with ticket details."""
        message = (
            f"*JIRA Update Notification:*,*Key:* {ticket['key']},*Summary:* {ticket['summary']},*Status:* {ticket['status']},*Last Updated:* {ticket['updated']},*Link:* <{ticket['url']}|{ticket['key']}>"
        )

        payload = {
            "channel": self.channel,
            "text": message
        }

        url = "https://slack.com/api/chat.postMessage"
        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
