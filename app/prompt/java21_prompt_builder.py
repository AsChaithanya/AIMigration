from app.prompt.base_prompt_builder import BasePromptBuilder


class Java21PromptBuilder(BasePromptBuilder):

    def build_prompt(self, request, cls, rag_context):

        prompt = []

        prompt.append("You are an expert Java modernization engineer.")

        prompt.append("")

        prompt.append("Goal")

        prompt.append("Upgrade the Java class from Java 8 to Java 21.")

        prompt.append("")

        prompt.append(f"Project : {request.metadata.project_name}")

        prompt.append(f"Class : {cls.name}")

        prompt.append("")

        prompt.append("Business Context")

        prompt.append(rag_context)

        prompt.append("")

        prompt.append("Requirements")

        prompt.append("- Preserve existing business logic")

        prompt.append("- Replace deprecated APIs")

        prompt.append("- Use Java 21 features where beneficial")

        prompt.append("- Improve readability without changing behaviour")

        return "\n".join(prompt)
 