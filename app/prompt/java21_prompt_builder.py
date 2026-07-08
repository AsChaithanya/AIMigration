from app.prompt.base_prompt_builder import BasePromptBuilder


class Java21PromptBuilder(BasePromptBuilder):

    def build_prompt(self, request, current_class, rag_context):

        source_version=request.metadata.source_version
        target_version=request.metadata.target_version

        prompt = []

        prompt.append("You are an expert Java modernization engineer.")

        prompt.append("")

        prompt.append("Goal")

        prompt.append(f"Upgrade the Java class from {source_version} to {target_version}.")

        prompt.append("")

        prompt.append(f"Project : {request.metadata.project_name}")

        prompt.append(f"Class : {current_class.name}")

        prompt.append("")

        prompt.append("Business Context")

        prompt.append(rag_context)

        prompt.append("")

        prompt.append("Requirements")

        prompt.append("- Preserve existing business logic")

        prompt.append("- Replace deprecated APIs")

        prompt.append(f"- Use {target_version} features where beneficial")

        prompt.append("- Improve readability without changing behaviour")

        return "\n".join(prompt)
 