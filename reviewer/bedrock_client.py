import boto3
import json
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

        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 700,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = self.client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(body)
        )

        response_body = json.loads(
            response["body"].read()
        )

        return response_body["content"][0]["text"]