from abc import ABC, abstractmethod
class RuleRepository(ABC):
   @abstractmethod
   def get_rules(self):
       pass