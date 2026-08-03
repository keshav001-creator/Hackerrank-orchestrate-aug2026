class DecisionEngine:

    def __init__(self):
        pass

    def make_decision(self, context):

        print("Decision Engine received:",
              context["message"]["message_id"])

        return None