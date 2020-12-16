#!/usr/local/bin/python3.9

# SPAWNING THREADS FOR COMPUTATION:
#   well, 1 thread, if you do anything computational expensive, tk will hang... so spawn a thread for work.. etc

############################################################################################
# NEXT Stream
# get rid of the hidden sub frame for records and only keep it visible as that is that frames purpose
# rename records frame to "ADD"
# flesh out the stats frame to show some nice visuals
#
############################################################################################

import tkinter as tk
from tkinter import Button, Entry
from tkinter.ttk import Notebook, Label, Frame
from PIL import Image, ImageTk
import pandas as pd
from datetime import datetime

dataFile = '../clocktime.csv'
df = pd.read_csv(dataFile)
today = datetime.today().strftime('%m/%d/%y')

def clickAddEntry():
    """DOCUMENTATION"""
    subfrEntryFields.pack()

def clickSubmitRecord():
    """DOCUMENTATION"""

    if recordDate_var.get() in df.values:
        row = df[df['date'] == today].index[0]

        df.loc[row, 'Lsec'] = df.loc[row, 'Lsec'] + int(recordProdSeconds_var.get())
        if df.loc[row, 'Lsec'] > 60:
            df.loc[row, 'Lmin'] = df.loc[row, 'Lmin'] + df.loc[row, 'Lsec']//60
            df.loc[row, 'Lsec'] = df.loc[row, 'Lsec'] % 60

        df.loc[row, 'Lmin'] = df.loc[row, 'Lmin'] + int(recordProdMinutes_var.get())
        if df.loc[row, 'Lmin'] > 60:
            df.loc[row, 'Lhour'] = df.loc[row, 'Lhour'] + df.loc[row, 'Lmin']//60
            df.loc[row, 'Lmin'] = df.loc[row, 'Lmin'] % 60

        df.loc[row, 'Lhour'] = df.loc[row, 'Lhour'] + int(recordProdHours_var.get())

        df.loc[row, 'Rsec'] = df.loc[row, 'Rsec'] + int(recordProdSeconds_var.get())
        if df.loc[row, 'Rsec'] > 60:
            df.loc[row, 'Rmin'] = df.loc[row, 'Rmin'] + df.loc[row, 'Rsec'] // 60
            df.loc[row, 'Rsec'] = df.loc[row, 'Rsec'] % 60

        df.loc[row, 'Rmin'] = df.loc[row, 'Rmin'] + int(recordProdMinutes_var.get())
        if df.loc[row, 'Rmin'] > 60:
            df.loc[row, 'Rhour'] = df.loc[row, 'Rhour'] + df.loc[row, 'Rmin'] // 60
            df.loc[row, 'Rmin'] = df.loc[row, 'Rmin'] % 60

        df.loc[row, 'Rhour'] = df.loc[row, 'Rhour'] + int(recordProdHours_var.get())

        # The final overwrite of the CSV
        df.to_csv('../test.csv', index=False)
    elif recordDate_var.get() not in df.values:
        newRecord = {
            'date': recordDate_var.get(),
            'Lhour': int(recordProdHours_var.get()),
            'Lmin': int(recordProdMinutes_var.get()),
            'Lsec': int(recordProdSeconds_var.get()),
            'Rhour': int(recordNonProdHours_var.get()),
            'Rmin': int(recordNonProdMinutes_var.get()),
            'Rsec': int(recordNonProdSeconds_var.get())
        }

        newdf = df.append(newRecord, ignore_index=True)
        # The final overwrite of the CSV
        newdf.to_csv(dataFile, index=False)

    # Clear the entry fields after a successful writing to the data file
    inputProdSeconds.delete(0, 'end')
    inputProdMinutes.delete(0, 'end')
    inputProdHours.delete(0, 'end')
    inputNonProdSeconds.delete(0, 'end')
    inputNonProdMinutes.delete(0, 'end')
    inputNonProdHours.delete(0, 'end')

    subfrEntryFields.pack_forget()

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
recordNonProdHours_var = tk.StringVar()
recordNonProdMinutes_var = tk.StringVar()
recordNonProdSeconds_var = tk.StringVar()

# This is where we build the different menu tabs
# These are menu tabs
splashScreen = Frame(tabControl)
recordMgmt = Frame(tabControl)
statCharts = Frame(tabControl)

# SPLASH SCREEN FRAME
row1 = Label(splashScreen, text=" ")
row1.config(font=("Norse", 300))
row1.pack(fill=tk.X)

lblWelcome = Label(splashScreen,
                   text="Welcome To The Productivity App!")
lblWelcome.config(font=("Norse", 40))
lblWelcome.pack()

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

## Render The menu buttons
subfrRecordMgmtButtons.pack(side=tk.TOP)

## SUB FRAME for the [Add] button entry fields
subfrEntryFields = Frame(recordMgmt)

### SUB SUB FRAME for the date entry input fields
subsubfrEntryFieldDate = Frame(subfrEntryFields)
entryFieldDateSpacer = Label(subsubfrEntryFieldDate, text=" ")
entryFieldDateSpacer.config(font=("Norse", 16))
entryFieldDateSpacer.pack()


lblDate = Label(subsubfrEntryFieldDate, text="Date")
lblDate.config(font=("Norse", 16))
lblDate.pack()

inputDate = Entry(subsubfrEntryFieldDate,
                  textvariable=recordDate_var,
                  font=("Norse", 16, "italic"))
inputDate.insert(0, today)
inputDate.pack(side=tk.LEFT)

### Render
subsubfrEntryFieldDate.pack(side=tk.TOP)

### Spacing and labels for input fields
productiveTimeSpacer = Label(subfrEntryFields, text=" ")
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

### Spacing and labels for input fields
nonProductiveTimeSpacer = Label(subfrEntryFields, text=" ")
nonProductiveTimeSpacer.config(font=("Norse", 16))
nonProductiveTimeSpacer.pack()
nonProdLabel = Label(subfrEntryFields, text="Non-Productive Time")
nonProdLabel.config(font=("Norse", 30))
nonProdLabel.pack(side=tk.TOP)
nonProdDataLabels = Label(subfrEntryFields, text="Hours\t\t\tMinutes\t\t\tSeconds")
nonProdDataLabels.config(font=("Norse", 16))
nonProdDataLabels.pack(side=tk.TOP)

### SUB SUB FRAME for Non-Productivity Data Entry Fields
subsubfrEntryFieldsNonProductivity = Frame(subfrEntryFields)
### non-Productive Hours
inputNonProdHours = Entry(subsubfrEntryFieldsNonProductivity,
                       textvariable=recordNonProdHours_var,
                       font=("Norse", 16, "italic"))
inputNonProdHours.pack(side=tk.LEFT)
### non-Productive Minutes
inputNonProdMinutes = Entry(subsubfrEntryFieldsNonProductivity,
                         textvariable=recordNonProdMinutes_var,
                         font=("Norse", 16, "italic"))
inputNonProdMinutes.pack(side=tk.LEFT)
### non-Productive Seconds
inputNonProdSeconds = Entry(subsubfrEntryFieldsNonProductivity,
                         textvariable=recordNonProdSeconds_var,
                         font=("Norse", 16, "italic"))
inputNonProdSeconds.pack(side=tk.LEFT)
### Render
subsubfrEntryFieldsNonProductivity.pack(side=tk.TOP)

submitButtonTimeSpacer = Label(subfrEntryFields, text=" ")
submitButtonTimeSpacer.config(font=("Norse", 16))
submitButtonTimeSpacer.pack()



# entryFieldsProductivity = Frame(entryFields)
#
# entryFieldsProductivity.pack(side=tk.TOP)


submitRecord = Button(subfrEntryFields, text="Submit",
                      command=clickSubmitRecord)  # the submit button for the new entries
submitRecord.config(font=("Norse", 20))
submitRecord.pack(side=tk.TOP)

subfrEntryFields.pack(side=tk.TOP)
# END hidden record entry field frame

# This hides the whole entry field frame until the add button is clicked
subfrEntryFields.pack_forget()

# STATS FRAME
## SUB FRAME for stats visuals
subfrStats = Frame(statCharts)
subfrStats.pack(side=tk.TOP)


##================================================##
## Add fields to root and render in the main loop ##
##================================================##
tabControl.add(splashScreen, text='Welcome')
tabControl.add(recordMgmt, text='Records')
tabControl.add(statCharts, text='Stats')
tabControl.pack(expand=1, fill="both")
root.mainloop()
