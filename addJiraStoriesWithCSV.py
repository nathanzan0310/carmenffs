import pandas as pd
import config
from helper.getUserInfo import get_account_id_from_display_name
from helper.issue_maker import create_issue, convert_to_adf, create_stories_for_epic

# Read CSV file into pandas DataFrame
df = pd.read_csv('test.csv')

# Assignee display name
assignee_display_name = "Mohanapriya Swaminathan"

# Get account ID for the assignee
assignee_account_id = get_account_id_from_display_name(assignee_display_name)
if assignee_account_id is None:
    print(f"Failed to find account ID for '{assignee_display_name}'. Exiting.")
    exit()

# Iterate over each row in df and create epics and stories
for index, row in df.iterrows():
    if row['Detailed Project Timeline Required']:
        epic_name = row['Project']
        project_key = row['Jira Project']
        summary = epic_name
        description = row['Scope']
        story_points = float(row['Estimated Effort']) if pd.notna(row['Estimated Effort']) else None
        start_date = row['Start Date'] if pd.notna(row['Start Date']) else None
        end_date = row['End Date'] if pd.notna(row['End Date']) else None
        target_date = row['Estimated Delivery date'] if pd.notna(row['Estimated Delivery date']) else None

        # Prepare data for the API request
        epic_data = {
            "fields": {
                "project": {
                    "key": project_key
                },
                "summary": summary,
                "description": convert_to_adf(description),  # Convert description to ADF
                "issuetype": {
                    "name": "Epic"
                },
                config.EPIC_NAME_FIELD_ID: epic_name,  # Epic Name
                config.STORY_POINTS_FIELD_ID: story_points,  # Story Points
                config.START_DATE_FIELD_ID: start_date,  # Start Date
                config.DUE_DATE_FIELD_ID: end_date,  # End Date
                config.TARGET_END_FIELD_ID: target_date,  # Target Date
                "assignee": {
                    "id": assignee_account_id  # Assign epic to assignee by account ID
                }
            }
        }

        # Remove None values from epic_data
        epic_data['fields'] = {k: v for k, v in epic_data['fields'].items() if v is not None}

        # Create the epic and get its key
        epic_key = create_issue(epic_data)

        # Create stories for epic if epic was created successfully
        if epic_key:
            create_stories_for_epic(epic_key, project_key, assignee_account_id, epic_name)

        # Break after the first iteration for testing purposes
        break
