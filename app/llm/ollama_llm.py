import requests 
from app.llm.base_llm import BaseLLM

class OllamaLLM(BaseLLM):
   def generate(self, prompt: str) -> str:
       response = requests.post(
           "http://localhost:11434/api/generate",
           json={
               "model": "deepseek-coder",
               "prompt": prompt,
               "stream": False
           }
       )
       return response.json()["response"]