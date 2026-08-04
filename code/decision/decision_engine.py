from llm.gemini_client import GeminiClient
from prompt.prompt_builder import PromptBuilder


class DecisionEngine:

    def __init__(self):

        self.prompt_builder = PromptBuilder()
        self.gemini = GeminiClient()

    def make_decision(self, context):

        prompt = self.prompt_builder.build_prompt(context)

        response = self.gemini.generate(prompt)

        print(response)

        return response