import requests
import json
from helper import config
from helper.getUserInfo import get_account_id_from_display_name

query = {
    "jql": 'your query here',
    "maxResults": 100,
    "startAt": 0
}

response = requests.request(
    "GET",
    f"{config.JIRA_URL}/rest/api/3/search",
    headers=config.HEADERS,
    auth=config.AUTH,
    params=query
)

# print(response.json()["issues"])
for i in response.json()["issues"]:
    key = i["key"]
    sp = i["fields"][config.STORY_POINTS_FIELD_ID]
    _url = f"{config.API_URL}/{key}"
    payload = json.dumps({
        "fields": {
            'assignee': {
                'id': get_account_id_from_display_name('Manish')
            }
        }
        # "skipScreenCheck": True
    })
    response = requests.request(
        "PUT",
        _url,
        data=payload,
        headers=config.HEADERS,
        auth=config.AUTH
    )

    print(response.text)
    print(response.status_code)
