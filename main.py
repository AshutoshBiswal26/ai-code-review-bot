import json
import os

from github import Github

# Read GitHub token
github_token = os.getenv("GITHUB_TOKEN")

# Initialize GitHub client
g = Github(github_token)

# Repository name
repo_name = os.getenv("GITHUB_REPOSITORY")

# Event payload path
event_path = os.getenv("GITHUB_EVENT_PATH")

# Load GitHub event data
with open(event_path, "r") as file:
    event_data = json.load(file)

# Extract PR number
pr_number = event_data["pull_request"]["number"]

# Access repository
repo = g.get_repo(repo_name)

# Access pull request
pr = repo.get_pull(pr_number)

print("\n==============================")
print(f"Reviewing PR #{pr_number}")
print(f"PR Title: {pr.title}")
print("==============================\n")

# Get changed files
files = pr.get_files()

for file in files:
    print(f"File: {file.filename}")
    print(f"Additions: {file.additions}")
    print(f"Deletions: {file.deletions}")

    print("\nPatch:")
    print(file.patch)

    print("\n" + "=" * 60 + "\n")