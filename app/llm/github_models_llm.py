import os
import requests
from app.llm.base_llm import BaseLLM

class GitHubLLM(BaseLLM):
   def __init__(self):
       self.endpoint = "https://models.inference.ai.azure.com/chat/completions"
       self.model = "gpt-4.1"
       self.token = os.getenv("GITHUB_TOKEN")
   def generate(self, prompt: str) -> str:
       headers = {
           "Authorization": f"Bearer {self.token}",
           "Content-Type": "application/json"
       }
       payload = {
           "model": self.model,
           "messages": [
               {
                   "role": "user",
                   "content": prompt
               }
           ],
           "temperature": 0.1
       }
       response = requests.post(
           self.endpoint,
           headers=headers,
           json=payload
       )
       print(response.status_code)
       print(response.text)
       response.raise_for_status()
       return response.json()["choices"][0]["message"]["content"]