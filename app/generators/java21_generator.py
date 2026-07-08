from app.generators.base_generator import BaseGenerator
from app.rules.path_rule_engine import PathRuleEngine

class Java21Generator(BaseGenerator):
    def generate(self, request, ai_responses=None):
        generated_files = []
        for file in request.files:
            for cls in file.classes:
                # If AI has already generated code, use it
                if ai_responses and cls.name in ai_responses:
                    file_content = ai_responses[cls.name]
                else:
                    # Otherwise generate using rules
                    file_content = self.generate_class(
                        cls,
                        request.relationships
                    )

                target_path= PathRuleEngine().get_target_path(file_metadata=file, target_language="Java21")

                generated_files.append({
                    "fileName": f"{cls.name}.java",
                    "content": file_content,
                    "targetPath": target_path
                })
        return generated_files

    def generate_class(self, cls, relationships):
        lines = []
        # Using statements
        lines.append("import java.util.*;")
        lines.append("")
        # Package declaration
        lines.append("package convertedproject;")
        lines.append("")
        # Parent class
        parent = None
        if cls.extends:
            parent = cls.extends
        inherits = []
        if parent:
            inherits.append(parent)
        # Interfaces
        if cls.implements:
            for interface in cls.implements:
                inherits.append(interface)
        if inherits:
            lines.append(f"public class {cls.name} extends {', '.join(inherits)}")
        else:
            lines.append(f"public class {cls.name}")
        lines.append("{")
        # Fields
        if cls.fields:
            for field in cls.fields:
                field_type = field.type if field.type else "Object"
                lines.append(f"    private {field_type} {field.name};")