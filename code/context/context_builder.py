class ContextBuilder:

    def __init__(self, loader):
        self.loader = loader

    def get_user(self, user_id):

        users = self.loader.users

        user = users[users["user_id"] == user_id]

        return user.iloc[0]

    def build_context(self, message):

        user = self.get_user(message["user_id"])
        group = self.get_group(message["group_id"])
        business = self.get_business(message["business_id"])
        history = self.get_history(message)

        return {
            "message": message,
            "user": user,
            "group": group,
            "business": business,
            "history": history
        }

    def get_group(self, group_id):

        if group_id is None:
            return None
    
        groups = self.loader.groups
    
        group = groups[groups["group_id"] == group_id]
    
        if group.empty:
            return None
    
        return group.iloc[0]

    def get_business(self, business_id):

        if business_id is None:
            return None
    
        businesses = self.loader.business_accounts
    
        business = businesses[
            businesses["business_id"] == business_id
        ]
    
        if business.empty:
            return None
    
        return business.iloc[0]

    def get_history(self, message):

        history = self.loader.message_history
    
        previous_messages = history[
            history["user_id"] == message["user_id"]
        ]
    
        return previous_messages