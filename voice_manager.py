import speech_recognition as sr
import pyttsx3
import logging
import settings

logger = logging.getLogger(__name__)


class VoiceManager:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 1

        self.vocalizing_engine = pyttsx3.init('sapi5')
        self.voices = self.vocalizing_engine.getProperty('voices')
        self.vocalizing_engine.setProperty('voice', self.voices[1].id)

    def speak(self, text):
        logger.info(f"Speaking: {text}")
        self.vocalizing_engine.say(text)
        self.vocalizing_engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            logger.info("Listening...")
            return self.recognizer.listen(source)

    def recognize(self, audio):
        try:
            logger.info("Recognizing...")
            query = self.recognizer.recognize_google(audio, language="ru-in")
        except Exception as e:
            logger.error(f"Can't recognize the text: {e}")
            return None
        logger.info(f"Received command: {query}")
        return query

    def take_command(self):
        audio = self.listen()
        command = self.recognize(audio)
        return command
