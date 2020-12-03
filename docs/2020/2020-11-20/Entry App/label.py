#!/usr/local/bin/python3.9


from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)




        text = Label(self, text="Just do it")
        text.place(relx=.5, rely=.5, anchor="center")
        #text.pack()

root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("200x200")
root.mainloop()
