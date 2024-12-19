# Slack/JIRA Integration Tool

This is a standalone application that integrates JIRA and Slack to monitor changes in a JIRA project and notify a Slack user about updates.

## Features
- Polls a specified JIRA project periodically for newly created or updated tickets.
- Sends a Slack Direct Message (DM) to a specified user when a ticket is created or updated.
- Includes ticket key, summary, status, timestamp of the last update, and a link to the JIRA ticket in the notification.

---

## Prerequisites
1. **JIRA Account**
   - Create a free JIRA account via [Atlassian](https://id.atlassian.com/).
   - Generate an API token via your Atlassian account settings.

2. **Slack Account**
   - Create a free Slack account via [Slack](https://slack.com/).
   - Create a Slack app via the [Slack API Console](https://api.slack.com/apps).
   - Generate an OAuth token with the `chat.write` scope.

3. **Python Environment**
   - Ensure Python 3.7+ is installed.
   - Install dependencies from `requirements.txt`.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/chavanabhi9888/Integration-of-slack-with-JIRA.git
   cd test-integration
pip install -r requirements.txt
2. Set Up Configuration: Create a .env file in the project directory with the following details:
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_API_TOKEN=your-jira-api-token
JIRA_EMAIL=your-jira-email
JIRA_PROJECT_KEY=your-project-key

SLACK_BOT_TOKEN=your-slack-bot-token
SLACK_USER_ID=target-slack-user-id

POLLING_INTERVAL=60  # Polling interval in seconds


Run the application:

python app.py



How It Works
The application polls the specified JIRA project at regular intervals (default: 60 seconds).
It checks for newly created or updated tickets since the last poll.
When a new or updated ticket is detected, it sends a DM to the configured Slack user with ticket details.
