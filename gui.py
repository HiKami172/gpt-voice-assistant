import settings

import customtkinter as ctk

from threading import Thread


class VoiceAssistant(Thread):

    def run(self):
        pass


class App(ctk.CTk):
    class ProgramsRegistry(ctk.CTkFrame):
        def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)
            self.add_program_btn = ctk.CTkButton(self, text="Add Program", command=self.add_program)
            self.programs_list = ctk.CTkFrame(self)

        def pack(self, **kwargs):
            super().pack(**kwargs)
            self.add_program_btn.pack(side=ctk.LEFT)
            self.programs_list.pack(side=ctk.LEFT)

        def add_program(self):
            dialog = ctk.CTkInputDialog(text="Type in a number:", title="Test")
            text = dialog.get_input()
            new_entry = self.ProgramEntry(self.programs_list)
            new_entry.pack(side=ctk.TOP)

        class ProgramEntry(ctk.CTkFrame):
            def __init__(self, master, **kwargs):
                super().__init__(master, **kwargs)
                self.name_entry = ctk.CTkEntry(self)
                self.path_entry = ctk.CTkEntry(self)
                self.browse_btn = ctk.CTkButton(self, text="Browse", command=self.browse)

            def pack(self, **kwargs):
                super().pack(**kwargs)
                self.name_entry.pack(side=ctk.LEFT)
                self.path_entry.pack(side=ctk.LEFT)
                self.browse_btn.pack(side=ctk.LEFT)

            def browse(self):
                pass

    def __init__(self):
        super().__init__()

        self.title(settings.APP_TITLE)
        self.iconbitmap(settings.ICON_PATH)
        self.minsize(settings.MIN_WIDTH, settings.MIN_HEIGHT)

        self.settings_menu = ctk.CTkButton(self, text="Settings", command=self.open_settings())
        self.settings_menu.pack(side=ctk.RIGHT)

        # self.ask_btn = ctk.CTkButton(self, text='Talk', width=100, height=100, command=self.take_command)
        # self.ask_btn.place(relx=0.5, rely=0.5, anchor='center')

    # Function to open the settings dialog
    def open_settings(self):
        settings_dialog = ctk.CTkToplevel(self)
        settings_dialog.title("Settings")

        # Add settings options or configuration widgets here
        programs_registry = self.ProgramsRegistry(settings_dialog)
        programs_registry.pack()
        settings_dialog.grab_set()  # Prevent interaction with main window while settings dialog is open


if __name__ == '__main__':
    app = App()
    app.mainloop()
