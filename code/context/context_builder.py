class ContextBuilder:

    def __init__(self, loader):
        self.loader = loader

    def get_user(self, user_id):

        users = self.loader.users

        user = users[users["user_id"] == user_id]

        return user.iloc[0]

    def build_context(self, message):

        user = self.get_user(message["user_id"])

        return {
            "message": message,
            "user": user
        }