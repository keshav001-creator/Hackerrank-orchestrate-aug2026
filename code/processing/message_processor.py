from context.context_builder import ContextBuilder
from decision.decision_engine import DecisionEngine
from output.csv_writer import CSVWriter

class MessageProcessor:

    def __init__(self, loader):
        self.loader = loader
        self.writer = CSVWriter()
        self.context_builder = ContextBuilder(loader)
        self.decision_engine = DecisionEngine()

    def process_messages(self):

        for index, (_, message) in enumerate(self.loader.messages.iterrows()):

             print(index)
             if index >= 2: 
                 break

             context = self.context_builder.build_context(message)
             decision = self.decision_engine.make_decision(context)
             
             self.writer.add_result(
                 context["message"]["message_id"],
                 decision
             )

        self.writer.save()

            # print("Decision for message : ", decision)


            # print("-----------------------")
            # print("Message :", context["message"]["message_id"])
            # print("User    :", context["user"]["user_id"])
            # print("History Messages :", len(context["history"]))
            
            # if context["group"] is not None:
            #     print("Group   :", context["group"]["group_id"])

            # if context["business"] is not None:
            #   print("Business:", context["business"]["business_id"])
