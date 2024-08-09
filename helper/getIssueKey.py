import requests
from helper import config


def search_issue_by_title(summary, project_key, issue_type='Epic'):
    # summary and title are the same in Jira
    jql = f'project = {project_key} AND summary ~ "{summary}" AND issuetype = {issue_type}'
    search_url = f"{config.JIRA_URL}/rest/api/3/search"
    params = {
        "jql": jql,
        "fields": "key",
        "maxResults": 1
    }
    response = requests.get(search_url, headers=config.HEADERS, auth=config.AUTH, params=params)
    response.raise_for_status()
    issues = response.json().get('issues', [])
    return issues[0]['key'] if issues else None


if __name__ == '__main__':
    print(search_issue_by_title('Farewell Tencent', 'SNP'))