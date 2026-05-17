from reviewer.prompts import REVIEW_PROMPT


class ReviewEngine:

    def generate_mock_review(self, patch):

        review_comments = []

        patch_lower = patch.lower()

        if "print(" in patch_lower:
            review_comments.append(
                "Consider using structured logging instead of print statements."
            )

        if "password" in patch_lower:
            review_comments.append(
                "Potential security concern: hardcoded password detected."
            )

        if len(patch) > 500:
            review_comments.append(
                "Large patch detected. Consider splitting into smaller PRs."
            )

        if not review_comments:
            review_comments.append(
                "Code changes look clean overall."
            )

        return review_comments

    def review_files(self, files):

        print("\n")
        print(REVIEW_PROMPT)
        print("\n")

        for file in files:

            print("=" * 60)

            print(f"File: {file['filename']}")
            print(f"Additions: {file['additions']}")
            print(f"Deletions: {file['deletions']}")

            print("\nPatch:\n")
            print(file["patch"])

            print("\nAI Review:\n")

            review_comments = self.generate_mock_review(
                file["patch"]
            )

            for comment in review_comments:
                print(f"- {comment}")

            print("\n" + "=" * 60 + "\n")