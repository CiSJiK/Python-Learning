import tkintersetup as tk # Need tkintersetup.py file in same directory.
import time as t

def change_color():
    tk.window.configure(background="grey")

def countdown():
    countlabel.configure(background="white")
    num = int(textbox.get())
    for i in range(num, 0, -1):
        countlabel.configure(text=i)
        tk.window.update()
        t.sleep(1)
    countlabel.configure(text="끝!")

red = tk.tkinter.Button(tk.window, text="Red", bg="red", command=change_color)
red.pack()

yellow = tk.tkinter.Button(tk.window, text="Yellow", bg="yellow")
yellow.pack()

green = tk.tkinter.Button(tk.window, text="Green", bg="green")
green.pack()

textbox = tk.tkinter.Entry(tk.window)
textbox.pack()

colorlabel = tk.tkinter.Label(tk.window, height = "10", width="10")
colorlabel.pack()

lbl = tk.tkinter.Label(tk.window, text="몇 초를 카운트다운 하시겠습니까?")
lbl.pack()

textbox = tk.tkinter.Entry(tk.window)
textbox.pack()

count = tk.tkinter.Button(tk.window, text="카운트다운!", command=countdown)
count.pack()

countlabel = tk.tkinter.Label(tk.window, height="10", width="10")
countlabel.pack()

tk.window.mainloop()