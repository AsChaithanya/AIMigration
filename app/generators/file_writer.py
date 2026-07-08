from pathlib import Path

class FileWriter:
   def write(self, project_name, generated_files):
    
       root = Path("output") / project_name 
       for file in generated_files:
           target_path = Path(file["targetPath"])
           file_path = root / target_path
           
           file_path.parent.mkdir(parents=True, exist_ok=True)
           with open(file_path, "w", encoding="utf-8") as f:
               f.write(file["content"])
       return str(root.parent)
   
