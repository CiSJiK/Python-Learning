import tkintersetup as tk # Need tkintersetup.py file in same directory.

red = tk.tkinter.Button(tk.window, text="Red", bg="red")
red.pack()

yellow = tk.tkinter.Button(tk.window, text="Yellow", bg="yellow")
yellow.pack()

green = tk.tkinter.Button(tk.window, text="Green", bg="green")
green.pack()

textbox = tk.tkinter.Entry(tk.window)
textbox.pack()

colorlabel = tk.tkinter.Label(tk.window, height = "10", width="10")
colorlabel.pack()

tk.window.mainloop()