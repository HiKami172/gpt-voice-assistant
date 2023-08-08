import unittest

from voice_manager import VoiceManager
from gpt_interface import GPTConversation
import settings
import utility_functions as uf

# TODO write tests for all modules

def run_assistant_loop():
    voice_manager = VoiceManager()
    conversation = GPTConversation(
        model=settings.OPENAI_MODEL,
        functions=[uf.get_current_weather, uf.spotify_play_song]
    )
    while True:
        input()
        command = voice_manager.take_command()
        answer = conversation.send_user_message(command)
        voice_manager.speak(answer)


if __name__ == '__main__':
    run_assistant_loop()
