from prompt.prompt_builder import PromptBuilder

class DecisionEngine:

    def __init__(self):
        self.prompt_builder = PromptBuilder()


    def make_decision(self, context):

        prompt = self.prompt_builder.build_prompt(context)

        print(prompt)

        return None