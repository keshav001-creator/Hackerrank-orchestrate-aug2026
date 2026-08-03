class PromptBuilder:

    def build_prompt(self, context):

        prompt = f"""
You are an AI Message Notification Router.

Current Message:
{context["message"]}

User:
{context["user"]}

Group:
{context["group"]}

Business:
{context["business"]}

History:
{context["history"]}

Decide:
1. action (notify, digest, mute)
2. message_type
3. reason
3. confidence
4. evidence_message_ids
"""

        return prompt