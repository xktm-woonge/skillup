# model/realtime_communication.py

from PyQt5.QtCore import QThread, pyqtSignal
from aiortc import RTCPeerConnection, RTCSessionDescription, RTCDataChannel
import asyncio

class RealtimeCommunicationModel(QThread):
    chatMessageReceived = pyqtSignal(str)
    fileReceived = pyqtSignal(bytes)
    voiceReceived = pyqtSignal(bytes)
    videoReceived = pyqtSignal(bytes)

    def __init__(self):
        super().__init__()
        self.pc = RTCPeerConnection()
        self.pc.on("datachannel", self.on_datachannel)

    def on_datachannel(self, channel):
        if channel.label == "chat":
            channel.on("message", self.chatMessageReceived.emit)
        elif channel.label == "file":
            channel.on("message", self.fileReceived.emit)
        elif channel.label == "voice":
            channel.on("message", self.voiceReceived.emit)
        elif channel.label == "video":
            channel.on("message", self.videoReceived.emit)

    def run(self):
        # Run the asyncio loop for WebRTC
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_forever()

    # Sending methods
    def send_chat(self, message):
        chat_channel = self.pc.createDataChannel("chat")
        chat_channel.send(message)

    def send_file(self, file_data):
        file_channel = self.pc.createDataChannel("file")
        file_channel.send(file_data)

    def send_voice(self, voice_data):
        voice_channel = self.pc.createDataChannel("voice")
        voice_channel.send(voice_data)

    def send_video(self, video_data):
        video_channel = self.pc.createDataChannel("video")
        video_channel.send(video_data)
