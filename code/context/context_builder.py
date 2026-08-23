from media.media_processor import MediaProcessor

class ContextBuilder:

    def __init__(self, loader):
        self.loader = loader
        self.media_processor = MediaProcessor(loader)

    def build_context(self, message):

        user = self.loader.users[
            self.loader.users["user_id"] == message["user_id"]
        ].iloc[0]

        history = self.loader.message_history[
        (self.loader.message_history["user_id"] == message["user_id"]) &
        (self.loader.message_history["message_id"] != message["message_id"])
        ].tail(5)

        group = None

        if message["group_id"]:
            group_data = self.loader.groups[
                self.loader.groups["group_id"] == message["group_id"]
            ]

            if not group_data.empty:
                group = group_data.iloc[0]

        business = None

        if message["business_id"]:
            business_data = self.loader.business_accounts[
                self.loader.business_accounts["business_id"]
                == message["business_id"]
            ]

            if not business_data.empty:
                business = business_data.iloc[0]

        media = self.media_processor.process(message)

        return {
            "message": message,
            "user": user,
            "history": history,
            "group": group,
            "business": business,
            "media": media
        }