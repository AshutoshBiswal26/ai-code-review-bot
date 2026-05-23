import os

from reviewer.github_client import GitHubPRClient
from reviewer.review_engine import ReviewEngine


def main():

    github_mode = os.getenv("GITHUB_EVENT_PATH")

    if github_mode:

        github_client = GitHubPRClient()

        pr_details = github_client.get_pr_details()

        print("\n==============================")
        print(f"Reviewing PR #{pr_details['number']}")
        print(f"PR Title: {pr_details['title']}")
        print("==============================")

        changed_files = github_client.get_changed_files()

    else:

        print("Running in LOCAL TEST MODE")

        github_client = None

        changed_files = [
            {
                "filename": "sample.py",
                "additions": 5,
                "deletions": 1,
                "patch": """
+ def login(password):
+     print(password)
"""
            }
        ]

    review_engine = ReviewEngine()

    review_summary = review_engine.review_files(
        changed_files
    )

    print("\nGenerated Review:\n")
    print(review_summary)

    if github_client:

        github_client.post_review_comment(
            f"""
## 🤖 AI Code Review Bot

{review_summary}
"""
        )

        print("\nReview comment posted successfully.")


if __name__ == "__main__":
    main()