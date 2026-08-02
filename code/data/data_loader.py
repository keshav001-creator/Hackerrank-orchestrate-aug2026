from pathlib import Path
import pandas as pd

class DataLoader:

    def __init__(self):

        self.dataset_path = Path("dataset")

        self.messages = None
        self.users = None
        self.groups = None
        self.group_members = None
        self.business_accounts = None
        self.user_business_history = None
        self.message_history = None
        self.message_events = None
        self.images = None
        self.voice_notes = None
        self.daily_notification_summary = None

    def _load_csv(self, filename):
        file_path = self.dataset_path / filename
        return pd.read_csv(file_path)



    def load_all(self):
      self.messages = self._load_csv("messages.csv")
      self.users = self._load_csv("users.csv")
      self.groups = self._load_csv("groups.csv")
      self.group_members = self._load_csv("group_members.csv")
      self.business_accounts = self._load_csv("business_accounts.csv")
      self.user_business_history = self._load_csv("user_business_history.csv")
      self.message_history = self._load_csv("message_history.csv")
      self.message_events = self._load_csv("message_events.csv")
      self.images = self._load_csv("images.csv")
      self.voice_notes = self._load_csv("voice_notes.csv")
      self.daily_notification_summary = self._load_csv("daily_notification_summary.csv")
