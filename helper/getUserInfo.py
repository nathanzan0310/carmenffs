import requests
from requests.auth import HTTPBasicAuth
import json
import config

# Jira instance and authentication details
jira_url = config.JIRA_URL
api_url = f"{jira_url}/rest/api/3/myself"
user_search_url = f"{jira_url}/rest/api/3/user/search"
email = config.EMAIL
token = config.TOKEN
auth = HTTPBasicAuth(email, token)
headers = config.HEADERS


# Get account ID by display name
def get_account_id_from_display_name(display_name):
    query_params = {'query': display_name}
    response = requests.get(user_search_url, headers=headers, auth=auth, params=query_params)
    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user['displayName'] == display_name:
                return user['accountId']
    else:
        print(f"Failed to search for user '{display_name}'. Response: {response.text}")
    return None


response = requests.get(api_url, headers=headers, auth=auth)

if response.status_code == 200:
    user_info = response.json()
    print(json.dumps(user_info, indent=4))  # Pretty-print the JSON response
    username = user_info.get('name')  # This will get the username for server/DC instances
    account_id = user_info.get('accountId')  # This will get the account ID for cloud instances
    print(f"Username: {username}")
    print(f"Account ID: {account_id}")
else:
    print(f"Failed to fetch user information. Response: {response.text}")
