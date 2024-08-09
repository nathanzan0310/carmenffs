import pandas as pd
from helper import config
from helper.getUserInfo import get_account_id_from_display_name
from helper.issue_maker import create_issue, convert_to_adf, create_default_stories_for_epic
from helper.getIssueKey import search_issue_by_title

'''
CHANGE THIS FILE PATH TO YOUR OWN FILE PATH
'''
# Read CSV file into pandas DataFrame
df = pd.read_csv('test_data/test.csv')


# Iterate over each row in df and create epics and stories
for index, row in df.iterrows():
    issue_name = row['Issue Title']
    issue_type = row['Issue Type'].lower().capitalize()
    project_key = row['Jira Board']
    parent_name = row['Parent Name']  # This is the epic name in case of a story
    summary = issue_name
    description = row['Description']
    story_points = float(row['Story Points']) if pd.notna(row['Story Points']) else None
    assignee_account_ID = get_account_id_from_display_name(row['Assignee Display Name']) if pd.notna(
        row['Assignee Display Name']) else None
    co_assignee_account_ID = get_account_id_from_display_name(row['Co-Assignee Display Name']) if pd.notna(
        row['Co-Assignee Display Name']) else None
    start_date = row['Start Date'] if pd.notna(row['Start Date']) else None
    end_date = row['End Date'] if pd.notna(row['End Date']) else None
    target_date = row['Target Date'] if pd.notna(row['Target Date']) else None

    # Search for the epic by its name if it's a story
    parent_key = None
    if issue_type == 'Story' and parent_name:
        parent_key = search_issue_by_title(parent_name, project_key, issue_type='Epic')

    # Prepare data for the API request
    data = {
        "fields": {
            "project": {
                "key": project_key
            },
            "summary": summary,
            "description": convert_to_adf(description),  # Convert description to ADF
            "issuetype": {
                "name": issue_type
            },
            # config.ISSUE_NAME_FIELD_ID: issue_name,  # Issue Name
            config.STORY_POINTS_FIELD_ID: story_points,  # Story Points
            config.START_DATE_FIELD_ID: start_date,  # Start Date
            config.DUE_DATE_FIELD_ID: end_date,  # End Date
            config.TARGET_END_FIELD_ID: target_date,  # Target Date
            "assignee": {
                "id": assignee_account_ID  # Assign epic to assignee by account ID
            },
            config.CO_ASSIGNEE_FIELD_ID: co_assignee_account_ID,  # Co-Assignee
            "parent": {
                "key": parent_key  # Link to the epic using parent field
            }
        }
    }
    # Remove None values from data
    data['fields'] = {k: v for k, v in data['fields'].items() if v is not None}

    # Create issue and get its key
    issue_key = create_issue(data)

    if issue_type == 'Epic':
        # Create stories for epic if epic was created successfully
        if issue_key and row['Default Epic Stories']:
            create_default_stories_for_epic(issue_key, project_key, assignee_account_ID, issue_name)

    # Break after first iteration for testing purposes
    # break
