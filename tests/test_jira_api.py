import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_jira_api():
    base_url = os.getenv("JIRA_BASE_URL")
    api_token = os.getenv("JIRA_API_TOKEN")
    email = os.getenv("JIRA_EMAIL")
    project_key = os.getenv("JIRA_PROJECT_KEY")

    if not all([base_url, api_token, email, project_key]):
        print("Please ensure JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN, and JIRA_PROJECT_KEY are set in the .env file.")
        return

    auth = HTTPBasicAuth(email, api_token)
    headers = {"Content-Type": "application/json"}

    url = f"{base_url}/rest/api/3/project/{project_key}"

    try:
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 200:
            print("JIRA API is up and running!")
            # print(f"Project details: {response.json()}")
        else:
            print(f"Failed to connect: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_jira_api()
