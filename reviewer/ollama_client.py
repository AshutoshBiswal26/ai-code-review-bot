import requests


class OllamaClient:

    def __init__(self):

        self.base_url = "http://localhost:11434/api/generate"

        self.model = "gemma3:4b"

    def review_code(self, patch):

        prompt = f"""
You are an expert AI Code Reviewer.

Review the following GitHub Pull Request diff.

Rules:
- Be concise
- Give bullet points only
- Focus on:
  - bugs
  - security
  - readability
  - maintainability
- Maximum 5 comments
- Avoid long explanations
- Sound like a senior engineer reviewing a PR

Code Diff:
{patch}
"""

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:

            response = requests.post(
                self.base_url,
                json=payload
            )

            response.raise_for_status()

            response_json = response.json()

            print("\nDEBUG RESPONSE:")
            print(response_json)

            return response_json.get(
                "response",
                "No AI response generated."
            )

        except Exception as e:

            return f"Error generating AI review: {str(e)}"