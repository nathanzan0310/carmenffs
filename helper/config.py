# config.py

import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load environment variables from .env file
load_dotenv()

# Jira instance and authentication details
JIRA_URL = os.getenv("JIRA_URL")
API_URL = f"{JIRA_URL}/rest/api/3/issue"
USER_SEARCH_URL = f"{JIRA_URL}/rest/api/3/user/search"
EMAIL = os.getenv("EMAIL")
TOKEN = os.getenv("TOKEN")
AUTH = HTTPBasicAuth(EMAIL, TOKEN)
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Custom field IDs for my Jira instance
ISSUE_NAME_FIELD_ID = "customfield_10011"
STORY_POINTS_FIELD_ID = "customfield_10028"
START_DATE_FIELD_ID = "customfield_10015"
DUE_DATE_FIELD_ID = "duedate"
TARGET_END_FIELD_ID = "customfield_10023"
CO_ASSIGNEE_FIELD_ID = "customfield_10035"
