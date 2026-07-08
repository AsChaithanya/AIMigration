from app.rules.rule_repository import RuleRepository
class JavaUpgradeRules(RuleRepository):
   def get_rules(self):
       return {
           "Vector": "ArrayList",
           "Hashtable": "HashMap",
           "Date": "LocalDateTime",
           "Calendar": "LocalDateTime"
       }