from app.planner.dependency_planner import DependencyPlanner
from app.strategies.java_to_csharp_strategy import JavaToCSharpStrategy
from app.strategies.java_upgrade_strategy import JavaUpgradeStrategy

class MigrationAgent:
   def __init__(self):
       self.strategies = {
           "JAVA_TO_CSHARP": JavaToCSharpStrategy(),
           "JAVA_UPGRADE": JavaUpgradeStrategy()
       }
       self.dependency_planner = DependencyPlanner()
   
   def execute(self, request):
        migration_type = request.migration.migration_type
        strategy = self.strategies.get(migration_type)
        if strategy is None:
            return {
                "status": "FAILED",
                "message": f"Unsupported migration type: {migration_type}"
            }
        
        all_classes=[]
        for file in request.files:
            all_classes.extend(file.classes)
        migration_order = self.dependency_planner.build_plan(all_classes)
        print("Migration Order:", migration_order)
        return strategy.execute(request, migration_order)