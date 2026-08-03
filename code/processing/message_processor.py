from context.context_builder import ContextBuilder


class MessageProcessor:

    def __init__(self, loader):
        self.loader = loader
        self.context_builder = ContextBuilder(loader)

    def process_messages(self):

        for _, message in self.loader.messages.iterrows():

            context = self.context_builder.build_context(message)

            print("-----------------------")
            print("Message :", context["message"]["message_id"])
            print("User    :", context["user"]["user_id"])
            print("History Messages :", len(context["history"]))
            
            if context["group"] is not None:
                print("Group   :", context["group"]["group_id"])

            if context["business"] is not None:
              print("Business:", context["business"]["business_id"])
