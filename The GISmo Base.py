from tkinter import *
from tkinter import ttk

# Hello

root = Tk()
root.title("The GISmo")


mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

notes = ttk.Notebook(mainframe)
f1 = ttk.Frame(notes)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(notes)   # second page
notes.add(f1, text='Bum')
notes.add(f2, text='arse')

print ('hello..its all done')
