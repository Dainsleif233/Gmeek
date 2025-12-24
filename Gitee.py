import requests

class Gitee:
    def __init__(self, token, repo_name):
        self.token = token
        self.repo = repo_name

    def get_issues(self):
        api = f"https://gitee.com/api/v5/repos/{self.repo}/issues?access_token{self.token}&page=1&per_page=100"
        response = requests.get(api)
        if response.ok:
            return response.json()
        else:
            return []

    def get_labels(self):
        api = f"https://gitee.com/api/v5/repos/{self.repo}/labels?access_token={self.token}"
        response = requests.get(api)
        if response.ok:
            return response.json()
        else:
            return []