from llm.gemini_client import GeminiClient
from prompt.prompt_builder import PromptBuilder
from responseParser.response_parser import ResponseParser


class DecisionEngine:

    def __init__(self):

        self.prompt_builder = PromptBuilder()
        self.gemini = GeminiClient()
        self.parser= ResponseParser()

    def make_decision(self, context):

        prompt = self.prompt_builder.build_prompt(context)

        try:

           response = self.gemini.generate(prompt)
   
           print("RAW RESPONSE:")
           print(response)
           print("----------------")
   
           decision = self.parser.parse(response)
           
           print(decision)
           
           return decision

        except Exception as e:

            print("Error generating decision:", e)

            return {
            "action": "digest",
            "message_type": "unknown",
            "reason": f"Gemini failed: {str(e)}",
            "confidence": 0.0,
            "evidence_message_ids": []
           }