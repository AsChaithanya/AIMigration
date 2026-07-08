from app.llm.base_llm import BaseLLM


class MockLLM(BaseLLM):

    def generate(self, prompt: str) -> str:

        return f"""

// ==========================================

// MOCK AI GENERATED CODE

// ==========================================

/*

Prompt Received:

{prompt}

*/

public class GeneratedByMockAI

{{

}}

"""
 