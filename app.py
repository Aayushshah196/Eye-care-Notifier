import tkinter as tk
from tkinter import ttk
import json

class Window(tk.Tk):
    def _configure_widgets(self):
        self.close_status = 0
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        self.menu_file = tk.Menu(self.menubar, tearoff=0)
        self.menu_quit = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(menu=self.menu_file, label='Setting')
        self.menubar.add_cascade(menu=self.menu_quit, label='Quit')
        self.menu_quit.add_command(label='Quit', command=self._quit)

    def _quit(self):
        self.close_status = 1
        self.destroy()

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Eye Care Notifier")
        self._configure_widgets()

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, SettingPage):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

class MainPage(tk.Frame):

    def _create_widgets(self):
        self.label = tk.Label(self, text="Welcome to the Eye Care Notifier")
        self.label.pack(padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self._create_widgets()

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SettingPage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

class SettingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self._configure_widgets()

    def _configure_widgets(self):
        with open('settings.json', 'r') as f:
            settings = json.load(f)
        # Page Header
        self.lb1 = tk.Label(self, text="Configure your settings").grid(row=0, column=0)
        
        tk.Label(self, text=" ").grid(row=1, column=0)    
        
        self.lb2 = tk.Label(self, text="Short rest duration ").grid(row=2, column=1)
        self.e1 = tk.Entry(self)
        self.e1.grid(row=2, column=2)
        self.e1.insert(0, settings["short_rest"])
        self. lb3 = tk.Label(self, text="minutes.").grid(row=2, column=3)

        tk.Label(self, text=" ").grid(row=3, column=0)    

        self.lb4 = tk.Label(self, text="Long rest duration ").grid(row=4, column=1)
        self.e2 = tk.Entry(self)
        self.e2.insert(0, settings["long_rest"])
        self.e2.grid(row=4, column=2)
        self.lb5 = tk.Label(self, text="minutes.").grid(row=4, column=3)

        tk.Label(self, text=" ").grid(row=5, column=0)    

        self.lb6 = tk.Label(self, text="Notification duration ").grid(row=6, column=1)
        self.e3 = tk.Entry(self)
        self.e3.insert(0, settings["notification_duration"])
        self.e3.grid(row=6, column=2)
        self.lb7 = tk.Label(self, text="seconds.").grid(row=6, column=3)

        tk.Label(self, text=" ").grid(row=1, column=0)    
        tk.Label(self, text=" ").grid(row=8, column=0)    

        self.save_btn = tk.Button(self, text="Go to the Side Page", \
            command=lambda: self._save_changes(self.e1.get(), self.e2.get(), self.e3.get()))
        self.save_btn.grid(row=9, column=3)
        # self.save_btn.pack(side="bottom", fill=tk.X)

    def _save_changes(self, short_rest, long_rest, notification_duration):
        with open('settings.json', 'w') as f:
            json.dump({
                        "short_rest": int(short_rest),
                        "long_rest": int(long_rest),
                        "notification_duration": int(notification_duration)
            }, f)


if __name__ == "__main__":
    testObj = Window()
    testObj.mainloop()
