# controller/realtime_connector.py

from model.websocket_communication import RealtimeCommunicationModel

class RealtimeController:
    def __init__(self):
        self.rtc_model = RealtimeCommunicationModel()
        self.rtc_model.chatMessageReceived.connect(self.on_chat_received)
        self.rtc_model.fileReceived.connect(self.on_file_received)
        self.rtc_model.voiceReceived.connect(self.on_voice_received)
        self.rtc_model.videoReceived.connect(self.on_video_received)
        self.rtc_model.start()

    def on_chat_received(self, message):
        # Handle received chat message, maybe update the UI
        pass

    def on_file_received(self, file_data):
        # Handle received file data
        pass

    def on_voice_received(self, voice_data):
        # Handle received voice data
        pass

    def on_video_received(self, video_data):
        # Handle received video data
        pass

    def send_chat(self, message):
        self.rtc_model.send_chat(message)

    def send_file(self, file_data):
        self.rtc_model.send_file(file_data)

    def send_voice(self, voice_data):
        self.rtc_model.send_voice(voice_data)

    def send_video(self, video_data):
        self.rtc_model.send_video(video_data)
