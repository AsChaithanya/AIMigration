from app.prompt.base_prompt_builder import BasePromptBuilder

class CSharpPromptBuilder(BasePromptBuilder):
   def build_prompt(self, request, current_class, rag_context):
       prompt = []
       prompt.append("You are an expert Java to C# migration engineer.")
       prompt.append("")
       prompt.append("Goal")
       prompt.append("Convert the Java class into production-ready .NET 8 C#.")
       prompt.append("")
       prompt.append(f"Project : {request.metadata.project_name}")
       prompt.append(f"Class : {current_class.name}")
       prompt.append("")
       prompt.append("Business Context")
       prompt.append(rag_context)
       prompt.append("")
       prompt.append("Requirements")
       prompt.append("- Preserve business logic")
       prompt.append("- Follow .NET 8 conventions")
       prompt.append("- Use dependency injection where appropriate")
       prompt.append("- Generate clean C# code")
       return "\n".join(prompt)