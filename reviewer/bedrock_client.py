import boto3
import os


class BedrockClient:

    def __init__(self):

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=os.getenv(
                "AWS_REGION",
                "us-east-1"
            )
        )

        self.model_id = os.getenv(
            "BEDROCK_MODEL_ID"
        )

        print(f"Using model: {self.model_id}")

    def review_code(self, patch):

        prompt = f"""
You are a senior software engineer reviewing a GitHub Pull Request.

Review this code diff for:
- bugs
- readability
- maintainability
- security issues
- performance concerns

Provide concise actionable feedback.

Code Diff:
{patch}
"""

        response = self.client.converse(
            modelId=self.model_id,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            inferenceConfig={
                "maxTokens": 700,
                "temperature": 0.2
            }
        )

        return response["output"]["message"]["content"][0]["text"]