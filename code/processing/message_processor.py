from context.context_builder import ContextBuilder


class MessageProcessor:

    def __init__(self, loader):
        self.loader = loader
        self.context_builder = ContextBuilder(loader)

    def process_messages(self):

        for _, message in self.loader.messages.iterrows():

            context = self.context_builder.build_context(message)

            print(
            context["message"]["message_id"],
            context["user"]["user_id"]
          )