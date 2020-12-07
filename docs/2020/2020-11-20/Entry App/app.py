#!/usr/local/bin/python3.9

# SPAWNING THREADS FOR COMPUTATION:
#   well, 1 thread, if you do anything computational expensive, tk will hang... so spawn a thread for work.. etc

import tkinter as tk
from tkinter import Button, Entry
from tkinter.ttk import Notebook, Label, Frame
from PIL import Image, ImageTk

def clickAddEntry():
    """DOCUMENTATION"""
    pass  # TODO

def clickUpdateEntry():
    """DOCUMENTATION"""
    pass  # TODO

def clickShowCharts():
    """DOCUMENTATION"""
    pass  # TODO

def clickUndoAction():
    """DOCUMENTATION"""
    pass  # TODO

def showRecords():
    """DOCUMENTATION"""
    pass # TODO

def clickSubmitRecord():
    """DOCUMENTATION"""
    recordDate_var.get()
    recordProdHours_var.get()
    # recordProdMinutes_var.get()
    # recordProdSeconds_var.get()
    # recordUnProdHours_var.get()
    # recordUnProdMinutes_var.get()
    # recordUnProdSeconds_var.get()

    # to reset the value of the fields when dealing with the shifting of units ex: sec->Min->Hr
    # recordDate_var.set("")
    # recordProdHours_var.set()
    # recordProdMinutes_var.set()
    # recordProdSeconds_var.set()
    # recordUnProdHours_var.set()
    # recordUnProdMinutes_var.set()
    # recordUnProdSeconds_var.set()

    # TODO take these values and write to CSV

# Establish the Application instance
# Name the window's title
# Determine starting size and coordinates
# Enable tab control for the application
root = tk.Tk()
root.title("Productivity Data Tool")
root.geometry("850x800+200+200")
tabControl = Notebook(root)

# Create global variables for the applciation to use when adding a new record to the data file
# These are basically empty containers until we assign a value to them
recordDate_var = tk.StringVar()
recordProdHours_var = tk.StringVar()
recordProdMinutes_var = tk.StringVar()
recordProdSeconds_var = tk.StringVar()
recordUnProdHours_var = tk.StringVar()
recordUnProdMinutes_var = tk.StringVar()
recordUnProdSeconds_var = tk.StringVar()

# This is where we build the different menu tabs
# These are menu tabs
splashScreen = Frame(tabControl)
recordMgmt = Frame(tabControl)
statCharts = Frame(tabControl)

# SPLASH SCREEN FRAME
row1 = Label(splashScreen, text=" ")
row1.config(font=("Norse", 300))
row1.pack(fill=tk.X)

welcome_label = Label(splashScreen,
                      text="Welcome To The Productivity App!")
welcome_label.config(font=("Norse", 40))
welcome_label.pack()

# Load chess timer image
load = Image.open("timer.png")
load = load.resize((50, 50), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(splashScreen, image=render)
img.image = render
img.pack()

# RECORD MANAGEMENT FRAME
## SUB FRAME for record management buttons
subfrRecordMgmtButtons = Frame(recordMgmt)

## create button, to add a record
btnAddEntry = Button(subfrRecordMgmtButtons,
                     text="Add",
                     command=clickAddEntry)
btnAddEntry.config(font=("Norse", 20))
btnAddEntry.pack(side=tk.LEFT)

## Create button to update a record
btnUpdateEntry = Button(subfrRecordMgmtButtons,
                        text="Update",
                        command=clickUpdateEntry)
btnUpdateEntry.config(font=("Norse", 20))
btnUpdateEntry.pack(side=tk.LEFT)

## Create button to activate visualizations
btnShowCharts = Button(subfrRecordMgmtButtons,
                       text="Stats",
                       command=clickShowCharts)
btnShowCharts.config(font=("Norse", 20))
btnShowCharts.pack(side=tk.LEFT)

## Create button to undo last action
btnUndoAction = Button(subfrRecordMgmtButtons,
                       text="Undo",
                       command=clickUndoAction)
btnUndoAction.config(font=("Norse", 20))
btnUndoAction.pack(side=tk.LEFT)

## Render The menu buttons
subfrRecordMgmtButtons.pack(side=tk.TOP)

## Button to show the records in the csv
btnShowRecords = Button(recordMgmt, text="Show Records", command=showRecords)
## glimpseRecords = Button(recordMgmt, text="Show Records", command=lambda: glimpseRecords.pack_forget())
btnShowRecords.config(font=("Norse", 20))
btnShowRecords.pack(side=tk.TOP)

## SUB FRAME for the [Add] button entry fields
subfrEntryFields = Frame(recordMgmt)

### SUB SUB FRAME for the date entry input fields
subsubfrEntryFieldDate = Frame(subfrEntryFields)
entryFieldDateSpacer = Label(subsubfrEntryFieldDate, text=" ")
entryFieldDateSpacer.config(font=("Norse", 16))
entryFieldDateSpacer.pack()

inputDate = Entry(subsubfrEntryFieldDate,
                  textvariable=recordDate_var,
                  font=("Norse", 16, "italic"))
inputDate.pack(side=tk.LEFT)

### Render
subsubfrEntryFieldDate.pack(side=tk.TOP)

### Spacing and labels for input fields
productiveTimeSpacer= Label(subfrEntryFields, text=" ")
productiveTimeSpacer.config(font=("Norse", 16))
productiveTimeSpacer.pack()
prodLabel = Label(subfrEntryFields, text="Productive Time")
prodLabel.config(font=("Norse", 30))
prodLabel.pack(side=tk.TOP)
prodDataLabels = Label(subfrEntryFields, text="Hours\t\t\tMinutes\t\t\tSeconds")
prodDataLabels.config(font=("Norse", 16))
prodDataLabels.pack(side=tk.TOP)

### SUB SUB FRAME for Productivity Data Entry Fields
subsubfrEntryFieldsProductivity = Frame(subfrEntryFields)
### Productive Hours
inputProdHours = Entry(subsubfrEntryFieldsProductivity,
                       textvariable=recordProdHours_var,
                       font=("Norse", 16, "italic"))
inputProdHours.pack(side=tk.LEFT)
### Productive Minutes
inputProdMinutes = Entry(subsubfrEntryFieldsProductivity,
                         textvariable=recordProdMinutes_var,
                         font=("Norse", 16, "italic"))
inputProdMinutes.pack(side=tk.LEFT)
### Productive Seconds
inputProdSeconds = Entry(subsubfrEntryFieldsProductivity,
                         textvariable=recordProdSeconds_var,
                         font=("Norse", 16, "italic"))
inputProdSeconds.pack(side=tk.LEFT)

### Render
subsubfrEntryFieldsProductivity.pack(side=tk.TOP)


# entryFieldsProductivity = Frame(entryFields)
#
# entryFieldsProductivity.pack(side=tk.TOP)


submitRecord = Button(subfrEntryFields, text="Submit", command=clickSubmitRecord) #the submit button for the new entries
submitRecord.config(font=("Norse", 20))
submitRecord.pack(side=tk.TOP)

subfrEntryFields.pack(side=tk.TOP)
# END hidden record entry field frame




##================================================##
## Add fields to root and render in the main loop ##
##================================================##
tabControl.add(splashScreen, text='Welcome')
tabControl.add(recordMgmt, text='Records')
tabControl.add(statCharts, text='Stats')
tabControl.pack(expand=1, fill="both")
root.mainloop()
