from app.rules.rule_repository import RuleRepository
class JavaToCSharpRules(RuleRepository):
   def get_rules(self):
       return {
           "String": "string",
           "int": "int",
           "Integer": "int",
           "long": "long",
           "Long": "long",
           "boolean": "bool",
           "Boolean": "bool",
           "double": "double",
           "Double": "double",
           "float": "float",
           "Float": "float",
           "List": "List",
           "ArrayList": "List",
           "HashMap": "Dictionary",
           "Map": "Dictionary",
           "Date": "DateTime"
       }