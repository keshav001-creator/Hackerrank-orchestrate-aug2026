class PromptBuilder:

    def build_prompt(self, context):

        prompt = f"""
You are an AI Message Notification Router.

Analyze the following WhatsApp message.

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

Return ONLY a valid JSON object.

Do NOT include:
- Markdown
- ```json
- Explanations
- Extra text

Use exactly this format:

{{
    "action": "notify",
    "message_type": "personal",
    "reason": "short explanation",
    "confidence": 0.95,
    "evidence_message_ids": []
}}

The action must be one of:
- notify
- digest
- mute
"""

        return prompt