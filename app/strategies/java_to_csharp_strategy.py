from app.generators.code_generator import CodeGenerator
from app.generators.csharp_generator import CSharpGenerator
from app.rules.java_to_csharp_rules import JavaToCSharpRules
from app.strategies.base_strategy import MigrationStrategy
from app.rules.rule_engine import RuleEngine
from app.generators.file_writer import FileWriter
from app.rag.rag_service import RAGService
from app.prompt.csharp_prompt_builder import CSharpPromptBuilder
from app.llm.llm_factory import LLMFactory
from app.rules.path_rule_engine import PathRuleEngine

class JavaToCSharpStrategy(MigrationStrategy):
      
   def __init__(self):
       self.rule_engine = RuleEngine()
       self.rule_engine.register(JavaToCSharpRules())
       self.generator = CSharpGenerator()
       self.file_writer = FileWriter()
       self.rag_service = RAGService()
       self.prompt_builder = CSharpPromptBuilder()
       self.llm= LLMFactory.create("github")  # Default to mock LLM provider
       
   def execute(self, request, migration_order):
        ai_responses = {}
        for file in request.files:
            for cls in file.classes:
                # Retrieve RAG context
                context = self.rag_service.retrieve_context(request, cls.name)
                # Build prompt
                prompt = self.prompt_builder.build_prompt(
                    request=request,
                    current_class=cls,
                    rag_context=context
                )
                # Call LLM
                response = self.llm.generate(prompt)
                ai_responses[cls.name] = response
                print(f"\n===== AI Response : {cls.name} =====")
                print(response)

        generated_files = self.generator.generate(
            request,
            ai_responses
        )

        output_folder = self.file_writer.write(
            request.metadata.project_name,
            generated_files
        )
        return {
            "status": "SUCCESS",
            "migrationOrder": migration_order,
            "outputFolder": output_folder,
            "generatedFiles": generated_files,
            "migrationType": "JAVA_TO_CSHARP",
            "message": "Java to C# migration completed successfully."
        }
   
   