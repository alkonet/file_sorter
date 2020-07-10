from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

#from tkinter import *

#root = Tk()
#root.title("Графическая программа на Python")
#root.geometry("400x300")
#
#root.mainloop()


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            if len(extension) > 1:
                if (extension[1].lower() = "jpg" or extension[1].lower() = "png" or extension[1].lower() = "svg"):
                    file = folder_track + "/" + filename
                    new_path = folder_dest_photo + "/" + filename
                    os.rename(file, new_path)
                elif (extension[1].lower() = "mp3" or extension[1].lower() = "wav" or extension[1].lower() = "aac")
                    file = folder_track + "/" + filename
                    new_path = folder_dest_music + "/" + filename
                    os.rename(file, new_path)

folder_track =
folder_dest_photo =
folder_dest_video =
folder_dest_music =

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while(true):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
