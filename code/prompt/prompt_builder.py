class PromptBuilder:

    def build_prompt(self, context):

        message = context["message"]
        user = context["user"]
        group = context["group"]
        business = context["business"]

        prompt = f"""
You are an AI Message Notification Router.

CURRENT MESSAGE
---------------
Message ID: {message["message_id"]}
Conversation Type: {message["conversation_type"]}
Sender User ID: {message["sender_user_id"]}
Created At: {message["created_at"]}
Message: {message["message_text"]}
Media Type: {message["media_type"]}
Media ID: {message["media_id"]}
Forwarded Count: {message["forwarded_count"]}

USER
----
User ID: {user["user_id"]}
Do Not Disturb: {user["do_not_disturb_window"]}

GROUP
-----
{group}

BUSINESS
--------
{business}

HISTORY
-------
{context["history"]}

TASK
----
Return ONLY valid JSON.

Fields:
- action (notify, digest, mute)
- message_type
- reason
- confidence
- evidence_message_ids
"""

        return prompt