import pandas as pd


class CSVWriter:

    def __init__(self):

        self.results = []

    def add_result(self, message_id, decision):

        self.results.append({

            "message_id": message_id,
            "action": decision["action"],
            "message_type": decision["message_type"],
            "reason": decision["reason"],
            "confidence": decision["confidence"],
            "evidence_message_ids": ",".join(
                decision["evidence_message_ids"]
            ) if decision["evidence_message_ids"] else "none"

        })

    def save(self):

        df = pd.DataFrame(self.results)

        df.to_csv("output.csv", index=False)