import os
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

class JiraClient:
    def __init__(self):
        self.base_url = os.getenv("JIRA_BASE_URL")
        self.api_token = os.getenv("JIRA_API_TOKEN")
        self.project_key = os.getenv("JIRA_PROJECT_KEY")
        self.jira_email = os.getenv("JIRA_EMAIL")
        self.headers = {
            # "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    def get_updated_tickets(self, last_poll_time):
        """Fetch tickets updated since the last poll time."""
        jql = f"project={self.project_key}"
        last_poll_time = datetime.strptime(last_poll_time, "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%Y-%m-%d %H:%M")
        if last_poll_time:
            jql += f" AND updated >= '{last_poll_time}'"

        url = f"{self.base_url}/rest/api/3/search"
        params = {
            "jql": jql,
            "fields": "key,summary,status,updated",
            "maxResults": 50
        }

        auth = HTTPBasicAuth(self.jira_email, self.api_token)
        response = requests.get(url, headers=self.headers, params=params, auth=auth)
        print(f"Response Status Code: {response.status_code}")
        print(f"self.headers: {self.headers}")
        print(f"Response Body: {response.text}")
        response.raise_for_status()
        data = response.json()

        tickets = []
        for issue in data.get("issues", []):
            tickets.append({
                "key": issue["key"],
                "summary": issue["fields"]["summary"],
                "status": issue["fields"]["status"]["name"],
                "updated": issue["fields"]["updated"],
                "url": f"{self.base_url}/browse/{issue['key']}"
            })

        return tickets