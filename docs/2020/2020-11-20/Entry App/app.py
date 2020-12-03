#!/usr/local/bin/python3.9

# NEXT STREAM:

# https://stackoverflow.com/questions/12364981/how-to-delete-tkinter-widgets-from-a-window#12365098

# Search: how to make an application with different pages

# https://www.delftstack.com/howto/python-tkinter/how-to-hide-recover-and-delete-tkinter-widgets/
# try:
#     import Tkinter as tk
# except:
#     import tkinter as tk
#
#
# class Test():
#     def __init__(self):
#         self.root = tk.Tk()
#         self.label = tk.Label(self.root,
#                               text="Label")
#         self.buttonForget = tk.Button(self.root,
#                                       text='Click to hide Label',
#                                       command=lambda: self.label.grid_forget())
#         self.buttonRecover = tk.Button(self.root,
#                                        text='Click to show Label',
#                                        command=lambda: self.label.grid())
#
#         self.buttonForget.grid(column=0, row=0, padx=10, pady=10)
#         self.buttonRecover.grid(column=0, row=1, padx=10, pady=10)
#         self.label.grid(column=0, row=2, padx=10, pady=10)
#         self.root.mainloop()
#
#     def quit(self):
#         self.root.destroy()
#
#
# app = Test()



from tkinter import *
from PIL import Image, ImageTk

# Define the window container for our app
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)



        # Welcome label
        welcome_label = Label(self, text="Welcome To The Productivity App!")
        welcome_label.place(relx=.28, rely=0, anchor="nw")
        welcome_label.config(font=("Norse", 40))

        # Load chess timer image
        load = Image.open("timer.png")
        load = load.resize((50, 50), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(relx=.2, rely=0, anchor="nw")

        #======= BUTTONS ========#

        # create button, link it to clickAddEntry()
        addEntry = Button(self, text="Add", command=self.clickAddEntry)
        addEntry.config(font=("Norse", 20))
        addEntry.place(relx=.05, rely=.1, anchor="ne")

        # Create button to delete a record
        deleteEntry = Button(self, text="Delete", command=self.clickDeleteEntry)
        deleteEntry.config(font=("Norse", 20))
        deleteEntry.place(relx=.07, rely=.134, anchor="ne")

        # Create button to update a record
        updateEntry = Button(self, text="Update", command=self.clickUpdateEntry)
        updateEntry.config(font=("Norse", 20))
        updateEntry.place(relx=.075, rely=.168, anchor="ne")

        # Create button to delete a record
        # deleteEntry = Button(self, text="Delete", command=self.deleteEntry)
        # deleteEntry.config(font=("Norse", 20))
        # deleteEntry.place(relx=.07, rely=.134, anchor="ne")
        #
        # # Create button to delete a record
        # deleteEntry = Button(self, text="Delete", command=self.deleteEntry)
        # deleteEntry.config(font=("Norse", 20))
        # deleteEntry.place(relx=.07, rely=.134, anchor="ne")

    def clickAddEntry(self):
        pass #TODO

    def clickDeleteEntry(self):
        pass #TODO

    def clickUpdateEntry(self):
        pass #TODO










root = Tk()
app = Window(root)


# set window title
root.wm_title("Tkinter window")
             # Resolution + starting coords
root.geometry("850x800+200+200")

# show window
app.mainloop()
