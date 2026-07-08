class RuleEngine:
   def __init__(self):
       self.rules = {}
   def register(self, rule_repository):
       self.rules.update(rule_repository.get_rules())
   def convert_type(self, java_type):
       return self.rules.get(java_type, java_type)