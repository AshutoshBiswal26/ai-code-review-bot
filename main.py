from reviewer.github_client import GitHubPRClient
from reviewer.review_engine import ReviewEngine


def main():

    github_client = GitHubPRClient()

    pr_details = github_client.get_pr_details()

    print("\n==============================")
    print(f"Reviewing PR #{pr_details['number']}")
    print(f"PR Title: {pr_details['title']}")
    print("==============================")

    changed_files = github_client.get_changed_files()

    review_engine = ReviewEngine()

    review_engine.review_files(changed_files)


if __name__ == "__main__":
    main()