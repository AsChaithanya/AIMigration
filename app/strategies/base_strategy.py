from abc import ABC, abstractmethod

class MigrationStrategy:
   def execute(self, request, migration_order):
       raise NotImplementedError("Subclasses must implement execute()")