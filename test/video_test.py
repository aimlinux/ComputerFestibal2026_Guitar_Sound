import tkinter as tk
from PIL import Image, ImageTk
import cv2

VIDEO_PATH = "video.mp4"

root = tk.Tk()
root.title("Guitar App")
root.geometry("800x500")

label = tk.Label(root)
label.place(x=0, y=0, relwidth=1, relheight=1)

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("動画が開けません。パスを確認してください。")

def update_frame():
    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (800, 500))

    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)

    label.imgtk = imgtk
    label.configure(image=imgtk)

    root.after(30, update_frame)

update_frame()

title = tk.Label(root, text="Guitar Sound Generator",
                 font=("Arial", 30),
                 bg="black", fg="white")
title.place(relx=0.5, rely=0.3, anchor="center")

root.mainloop()
