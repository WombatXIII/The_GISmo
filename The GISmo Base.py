
import tkinter as tk
from tkinter import *
from tkinter import ttk #apparently it needs both
from ScaleFrame import *

blarg = Tk()
blarg.title("Father Jack Simulator")

argyle = Frame(blarg)
argyle.grid(column=0, row=0, sticky=(N, W, E, S))
argyle.columnconfigure(0, weight=1)
argyle.rowconfigure(0, weight=1)
argyle.pack(pady=100, padx=100)


notes = ttk.Notebook(blarg)
f1 = ttk.Frame(notes)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(notes)   # second page
f3 = ttk.Frame(notes)
f4 = ttk.Frame(notes)

ScaleFrameClass = GisScaleFrame()
scaleFrame = ScaleFrameClass.GetScaleFrame(notes)

notes.add(f1, text='Gobshite!')
notes.add(f2, text='Arse')
notes.add(f3, text='Feck')
notes.add(f4, text='I love my brick')
notes.add(scaleFrame, text='Scale')
notes.pack(expand=1, fill="both")

ttk.Button(argyle, text="Quit", command=blarg.destroy).grid (column=1, row=1,sticky=E)

blarg.mainloop()