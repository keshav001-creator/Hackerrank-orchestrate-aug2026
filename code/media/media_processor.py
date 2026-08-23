class MediaProcessor:

    def __init__(self, loader):
        self.loader = loader

    def process(self, message):

        media_type = message["media_type"]
        media_id = message["media_id"]

        if not media_id:
            return None

        if media_type == "image":

            media = self.loader.images[
                self.loader.images["image_id"] == media_id
            ]

            if not media.empty:
                return {
                    "type": "image",
                    "data": media.iloc[0]
                }

        if media_type == "voice":

            media = self.loader.voice_notes[
                self.loader.voice_notes["voice_note_id"] == media_id
            ]

            if not media.empty:
                return {
                    "type": "voice",
                    "data": media.iloc[0]
                }

        return None