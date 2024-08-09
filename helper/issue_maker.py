import json

import requests

from helper import config


# Function to create a Jira issue
def create_issue(issue_data):
    response = requests.post(config.API_URL, headers=config.HEADERS, auth=config.AUTH, data=json.dumps(issue_data))
    if response.status_code == 201:
        issue_key = response.json()['key']
        issue_type = issue_data['fields']['issuetype']['name']
        if issue_type == 'Story':
            parent = issue_data['fields']['parent']['key']
            print(
                f"{issue_data['fields']['issuetype']['name']} '{issue_data['fields']['summary']}' created successfully with key {issue_key} under Epic {parent}.")
            return issue_key
        print(f"{issue_data['fields']['issuetype']['name']} '{issue_data['fields']['summary']}' created successfully "
              f"with key {issue_key}.")
        return issue_key
    else:
        print(f"Failed to create issue '{issue_data['fields']['summary']}'. Response: {response.text}")
        return None


# Convert plain text to Atlassian Document Format (ADF)
def convert_to_adf(text):
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": text
                    }
                ]
            }
        ]
    }


# Create stories for an epic
def create_default_stories_for_epic(epic_key, project_key, assignee_account_id, epic_name):
    story_summaries = ["Discovery", "Design", "Development", "UAT", "Hypercare"]
    for summary in story_summaries:
        story_data = {
            "fields": {
                "project": {
                    "key": project_key
                },
                "summary": summary + ": " + epic_name,
                "issuetype": {
                    "name": "Story"
                },
                "parent": {
                    "key": epic_key  # Link to the epic using parent field
                },
                "assignee": {
                    "id": assignee_account_id  # Assign the story to the assignee by account ID
                }
            }
        }
        create_issue(story_data)
