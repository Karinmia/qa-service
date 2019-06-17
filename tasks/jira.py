import requests

from ..diploma.settings.local import JIRA_LOGIN, JIRA_PASSWORD, JIRA_BASE_URL


class JiraClient:
    # def __init__(self, login, password, base_url):
    def __init__(self):
        self._login = JIRA_LOGIN
        self._password = JIRA_PASSWORD
        self._base_url = JIRA_BASE_URL

    def get_request(self, url):
        return requests.get(url, auth=(self._login, self._password))

    def post_request(self, url, body):
        return requests.post(url, json=body, auth=(self._login, self._password))

    def create_issue(self, project_key, summary, desc, issue_type):
        url = self._base_url + 'issue/'
        data = {'fields': {
            'project': {
                'key': project_key
            },
            'summary': summary,
            'description': desc,
            'issue_type': {
                'name': issue_type
            }
        }}
        result = self.post_request(url, data)
        if result.status_code is not 200:
            raise ApiError('Failed to create issue: ' + result.json())
        return result.json()

    def find_all_current_user_issues(self):
        url = self._base_url + 'search?jql=assignee={}+order+by+duedate'.format(self._login)
        result = self.get_request(url)
        if result.status_code is not 200:
            raise ApiError('Failed to find issues assigned to current users: ' + result.json())
        return result.json()['issues']

    def find_all_issues_qa_status(self):
        url = self._base_url + 'search?jql=status=QA'
        result = self.get_request(url)
        if result.status_code is not 200:
            raise ApiError('Failed to find issues with QA: ' + result.json())
        return result.json()['issues']

    def change_issue_status(self, issue, status_id, comment):
        url = self._base_url + 'issue/{}/transitions'.format(issue)
        data = {
            "update": {
                "comment": [
                    {
                        "add": {
                            "body": comment
                        }
                    }
                ]
            },
            "transition": {
                "id": status_id
            },
        }
        result = self.post_request(url, data)
        if result.status_code is not 200:
            raise ApiError('Failed to change issues status: ' + result.json())
        return True

    def get_issue_transitions(self, issue):
        url = self._base_url + 'issue/{}?expand=transitions'.format(issue)
        result = self.get_request(url)
        if result.status_code is not 200:
            raise ApiError('Failed to find issues with QA: ' + result.json())
        return result.json()['transitions']


class ApiError(BaseException):
    """
    Raised when some API specific error occurs (expired token,permission error etc.)
    :return: string with error message
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
