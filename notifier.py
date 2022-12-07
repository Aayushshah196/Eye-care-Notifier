import tkinter as tk
import time
import json

def notification_window(message, duration):
	window=tk.Tk()
	window.geometry("700x350")
	frame=tk.Frame(window, width=300, height=300)
	frame.grid(row=0, column=0, sticky="NW")

	label=tk.Label(window, text=message, font='Arial 17 bold')
	label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

	window.after(duration*1000, lambda: window.destroy())
	window.mainloop()

def notifier():

	with open("settings.json", "r") as f:
		settings = json.load(f)
	running = True
	state = 0

	while(running):
		time.sleep(settings["short_rest"])
		if state>settings["long_rest"]:
			notification_window("Time for a Long break", settings["notification_duration"])
		else:
			notification_window("Time for a short break", settings["notification_duration"])
		state += 1

if __name__ == "__main__":
	notification_window("Go for a walk", 10)