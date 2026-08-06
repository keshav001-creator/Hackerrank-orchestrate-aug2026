import json


class ResponseParser:

    def parse(self, response):

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        return json.loads(response)