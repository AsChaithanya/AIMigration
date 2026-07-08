import os

class PathRuleEngine:
   @staticmethod
   def get_target_path(file_metadata, metadata):
       package = file_metadata.package.lower()

       target=metadata.target_language.lower()
       if target == "c#":
           if "controller" in package:
               folder = "Controllers"
           elif "service" in package:
               folder = "Services"
           elif "repository" in package:
               folder = "Repositories"
           elif "model" in package or "entity" in package:
               folder = "Models"
           else:
               folder = "Common"
           return os.path.join(folder, file_metadata.name.replace(".java", ".cs"))
       elif target == "java21":
            return file_metadata.path
       else:
            return file_metadata.path