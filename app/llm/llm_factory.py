from app.llm.github_models_llm import GitHubLLM
from app.llm.mock_llm import MockLLM
from app.llm.ollama_llm import OllamaLLM
from app.llm.azure_openai_llm import AzureOpenAILLM

class LLMFactory:
   @staticmethod
   def create(provider: str):
       provider = provider.lower()
       if provider == "github":
           return GitHubLLM()
       if provider == "ollama":
           return OllamaLLM()
       if provider == "azure":
           return AzureOpenAILLM()
       if provider == "mock":
           return MockLLM()
       raise Exception(f"Unsupported LLM provider: {provider}")