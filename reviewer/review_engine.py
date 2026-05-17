from reviewer.bedrock_client import BedrockClient


class ReviewEngine:

    def __init__(self):

        self.bedrock_client = BedrockClient()

    def review_files(self, files):

        all_reviews = []

        for file in files:

            print(f"\nReviewing {file['filename']}")

            ai_review = self.bedrock_client.review_code(
                file["patch"]
            )

            formatted_review = f"""
### File: {file['filename']}

{ai_review}
"""

            all_reviews.append(formatted_review)

        return "\n\n".join(all_reviews)