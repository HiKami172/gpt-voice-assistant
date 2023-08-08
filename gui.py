import settings

import customtkinter as ctk

from threading import Thread


class VoiceAssistant(Thread):

    def run(self):
        pass


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(settings.APP_TITLE)
        self.iconbitmap(settings.ICON_PATH)
        self.minsize(settings.MIN_WIDTH, settings.MIN_HEIGHT)

        self.ask_btn = ctk.CTkButton(self, text='Talk', width=100, height=100, command=self.take_command)
        self.ask_btn.place(relx=0.5, rely=0.5, anchor='center')

    def take_command(self):
        voice_assistant_thread = VoiceAssistant()
        voice_assistant_thread.start()


if __name__ == '__main__':
    app = App()
    app.mainloop()
