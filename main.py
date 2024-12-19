import os
import time
import logging
from dotenv import load_dotenv
from modules.jira_client import JiraClient
from modules.slack_client import SlackClient

# Load environment variables
load_dotenv()

# Configuration
POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", 60))  # Default to 60 seconds
LAST_POLL_FILE = "last_poll.txt"

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def get_last_poll_time():
    """Read the last poll time from a file."""
    if os.path.exists(LAST_POLL_FILE):
        with open(LAST_POLL_FILE, 'r') as file:
            return file.read().strip()
    return None

def save_last_poll_time(timestamp):
    """Save the last poll time to a file."""
    with open(LAST_POLL_FILE, 'w') as file:
        file.write(timestamp)

def main():
    jira = JiraClient()
    slack = SlackClient()

    while True:
        last_poll_time = get_last_poll_time()
        logger.info("Polling JIRA for updates...")

        try:
            tickets = jira.get_updated_tickets(last_poll_time)
            logger.info(f"ticket...{tickets}")
            
            for ticket in tickets:
                slack.send_ticket_notification(ticket)
            
            if tickets:
                latest_update = max(ticket['updated'] for ticket in tickets)
                save_last_poll_time(latest_update)

        except Exception as e:
            logger.error(f"An error occurred: {e}")

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()