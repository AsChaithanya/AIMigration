from app.generators.code_generator import CodeGenerator
from app.generators.csharp_generator import CSharpGenerator
from app.generators.file_writer import FileWriter
from app.generators.java21_generator import Java21Generator
from app.llm.llm_factory import LLMFactory
from app.rag.rag_service import RAGService
from app.strategies.base_strategy import MigrationStrategy
from app.rules.rule_engine import RuleEngine
from app.rules.java_upgrade_rules import JavaUpgradeRules
from app.prompt.java21_prompt_builder import Java21PromptBuilder

class JavaUpgradeStrategy(MigrationStrategy):
    def __init__(self):
       self.rule_engine = RuleEngine()
       self.rule_engine.register(JavaUpgradeRules())
       self.generator = Java21Generator()
       self.file_writer = FileWriter()
       self.rag_service = RAGService()
       self.prompt_builder = Java21PromptBuilder()
       self.llm= LLMFactory.create("github")  # Default to mock LLM provider

    def execute(self, request,migration_order):

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

            "migrationType": "JAVA_UPGRADE",
            "status": "SUCCESS",
            "migrationOrder": migration_order,
            "outputFolder": output_folder,
            "generatedFiles": generated_files,
            "message": "Java upgrade rules loaded successfully."

        }
 