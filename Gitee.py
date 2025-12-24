import requests
from datetime import datetime


class GiteeLable:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color


class GiteeIssue:
    def __init__(
        self,
        number: str,
        title: str,
        body: str,
        labels: list,
        created_at: str,
        comments: int,
    ):
        self.number = number
        self.title = title
        self.body = body
        self.labels = [GiteeLable(label["name"], label["color"]) for label in labels]
        self.created_at = datetime.fromisoformat(created_at)
        self.comments = comments

    def get_events(self):
        return []

    def get_comments(self):
        return {"totalCount": self.comments}


class Gitee:
    def __init__(self, token, repo_name):
        self.token = token
        self.repo = repo_name

    def get_issues(self):
        api = f"https://gitee.com/api/v5/repos/{self.repo}/issues?access_token={self.token}&page=1&per_page=100"
        response = safe_request(api)
        if response:
            return [
                GiteeIssue(
                    issue["number"],
                    issue["title"],
                    issue["body"],
                    issue["labels"],
                    issue["created_at"],
                    issue["comments"],
                )
                for issue in response.json()
            ]
        else:
            return []

    def get_labels(self):
        api = f"https://gitee.com/api/v5/repos/{self.repo}/labels?access_token={self.token}"
        response = safe_request(api)
        if response:
            return [
                GiteeLable(label["name"], label["color"]) for label in response.json()
            ]
        else:
            return []


def safe_request(url, **kwargs):
    try:
        response = requests.get(url, **kwargs)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Request failed: {type(e).__name__}")
        return None
