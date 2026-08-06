class PromptBuilder:

    def build_prompt(self, context):

        message = context["message"]
        user = context["user"]
        group = context["group"]
        business = context["business"]

        prompt = f"""
You are an AI Message Notification Router.

Analyze the WhatsApp message below.

CURRENT MESSAGE
---------------
Message ID: {message["message_id"]}
Conversation Type: {message["conversation_type"]}
Sender Type: {message["sender_type"]}
Text: {message["message_text"]}
Timestamp: {message["timestamp"]}
Forward Count: {message["forwarded_count"]}

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
{len(context["history"])} previous related messages found.

TASK
----
Decide:

1. action → notify, digest or mute
2. message_type
3. reason
4. confidence
5. evidence_message_ids

Return ONLY valid JSON.
Do not return markdown or explanations.
"""

        return prompt