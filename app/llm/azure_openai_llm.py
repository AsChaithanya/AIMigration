from app.llm.base_llm import BaseLLM

class AzureOpenAILLM(BaseLLM):
   def generate(self, prompt: str) -> str:
       raise NotImplementedError(
           "Azure OpenAI integration pending."
       )