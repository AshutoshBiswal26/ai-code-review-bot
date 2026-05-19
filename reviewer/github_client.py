import json
import os

from github import Github


class GitHubPRClient:

    def __init__(self):

        github_token = os.getenv("GITHUB_TOKEN")

        self.github = Github(github_token)

        self.repo_name = os.getenv("GITHUB_REPOSITORY")

        self.event_path = os.getenv("GITHUB_EVENT_PATH")

        with open(self.event_path, "r") as file:
            self.event_data = json.load(file)

        self.pr_number = self.event_data["pull_request"]["number"]

        self.repo = self.github.get_repo(self.repo_name)

        self.pr = self.repo.get_pull(self.pr_number)

    def get_pr_details(self):

        return {
            "number": self.pr.number,
            "title": self.pr.title,
            "body": self.pr.body
        }

    def get_changed_files(self):

        changed_files = []

        files = self.pr.get_files()

        for file in files:

            changed_files.append({
                "filename": file.filename,
                "additions": file.additions,
                "deletions": file.deletions,
                "patch": file.patch
            })

        return changed_files

    def post_review_comment(self, comment):

        self.pr.create_issue_comment(comment)