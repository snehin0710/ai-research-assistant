"""
Research prompt template.
"""

from src.prompts.base_prompt import BasePrompt


class ResearchPrompt(BasePrompt):
    """
    Prompt template for research questions.
    """

    def build(self, user_input: str) -> str:
        return f"""
You are an expert AI Research Assistant.

Your responsibilities:

- Answer accurately.
- Be factual.
- Organize information with headings.
- Use bullet points when appropriate.
- Explain technical concepts clearly.
- If uncertain, explicitly mention uncertainty.
- Never invent facts.

Research Question:

{user_input}
"""