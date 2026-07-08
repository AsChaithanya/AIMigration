from abc import ABC, abstractmethod

class BasePromptBuilder(ABC):
   @abstractmethod
   def build_prompt(self, request, cls, rag_context):
       pass