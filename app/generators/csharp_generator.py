from app.generators.base_generator import BaseGenerator
from app.rules.path_rule_engine import PathRuleEngine

class CSharpGenerator(BaseGenerator):
   
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

                target_path= PathRuleEngine().get_target_path(file_metadata=file, metadata=request.metadata)

                generated_files.append({
                    "fileName": f"{cls.name}.cs",
                    "content": file_content,
                    "targetPath": target_path
                })
        return generated_files
   
   def generate_class(self, cls, relationships):
        lines = []
        # Using statements
        lines.append("using System;")
        lines.append("using System.Windows;")
        lines.append("")
        # Namespace
        lines.append("namespace ConvertedProject")
        lines.append("{")
        lines.append("")
        # Parent class
        parent = None
        if cls.extends:
            parent = cls.extends
            if parent == "JFrame":
                parent = "Window"
        inherits = []
        if parent:
            inherits.append(parent)
        # Interfaces
        if cls.implements:
            for interface in cls.implements:
                inherits.append(self.map_interface(interface))
        if inherits:
            lines.append(f"    public class {cls.name} : {', '.join(inherits)}")
        else:
            lines.append(f"    public class {cls.name}")
        lines.append("    {")
        # Fields
        if cls.fields:
            for field in cls.fields:
                field_type = self.map_type(field.type) if field.type else "object"
                lines.append(
                    f"        public {field_type} {field.name} {{ get; set; }}"
                )
        # Relationships
        if relationships:
            related = [
                r for r in relationships
                if r.from_class == cls.name and r.type == "uses"
            ]
            if related:
                lines.append("")
            for rel in related:
                lines.append(
                    f"        public {rel.to_class} {rel.to_class.lower()} {{ get; set; }}"
                )
        # Constructors
        if cls.constructors:
            for constructor in cls.constructors:
                params = []
                if constructor.parameters:
                    for p in constructor.parameters:
                        p_type = self.map_type(p.type)
                        params.append(f"{p_type} {p.name}")
                param_string = ", ".join(params)
                lines.append("")
                lines.append(f"        public {cls.name}({param_string})")
                lines.append("        {")
                lines.append("            // TODO: Constructor logic")
                lines.append("        }")
        # Methods
        if cls.methods:
            for method in cls.methods:
                # Skip Java main method
                if method.name == "main":
                    continue
                return_type = self.map_type(method.return_type)
                params = []
                if method.parameters:
                    for p in method.parameters:
                        ptype = self.map_type(p.type)
                        params.append(f"{ptype} {p.name}")
                param_string = ", ".join(params)
                visibility = method.visibility or "public"
                lines.append("")
                lines.append(
                    f"        {visibility} {return_type} {method.name}({param_string})"
                )
                lines.append("        {")
                lines.append(
                    f"            // {method.summary or 'TODO: Implement'}"
                )
                lines.append("        }")
        # Close class
        lines.append("    }")
        # Close namespace
        lines.append("}")
        return "\n".join(lines)
   
   def map_type(self, java_type):
    if not java_type:
        return "void"
    mapping = {
        "String": "string",
        "int": "int",
        "Integer": "int",
        "double": "double",
        "float": "float",
        "boolean": "bool",
        "long": "long",
        "JFrame": "Window",
        "JButton": "Button",
        "JTextField": "TextBox",
        "JComboBox": "ComboBox",
        "ActionEvent": "RoutedEventArgs",
    }
    return mapping.get(java_type, java_type)
   
   def map_interface(self, interface):
        mapping = {
            "ActionListener": "IActionListener",
            "Serializable": "ISerializable",
            "Runnable": "IRunnable",
            "Comparable": "IComparable",
            "Cloneable": "ICloneable",
            "Iterable": "IEnumerable",
            "Observer": "IObserver",
            "Observable": "IObservable",
            "EventListener": "IEventListener",
            "MouseListener": "IMouseListener",
            "KeyListener": "IKeyListener",
            "FocusListener": "IFocusListener",
            "WindowListener": "IWindowListener",
            "ComponentListener": "IComponentListener",
            "ItemListener": "IItemListener",
            "AdjustmentListener": "IAdjustmentListener",
            "TextListener": "ITextListener"
        }
        return mapping.get(interface, interface)