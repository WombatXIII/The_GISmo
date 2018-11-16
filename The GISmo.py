
import tkinter as tk
from tkinter import *
from tkinter import ttk #apparently it needs both
from ScaleFrame import *
from inches_to_mm import *
from Length import *

blarg = Tk()
blarg.title("The GISmo")

argyle = Frame(blarg)
argyle.grid(column=0, row=0, sticky=(N, W, E, S))
argyle.columnconfigure(0, weight=1)
argyle.rowconfigure(0, weight=1)
argyle.pack(pady=100, padx=100)


notes = ttk.Notebook(blarg)

ScaleFrameClass = GisScaleFrame()
scaleFrame = ScaleFrameClass.GetScaleFrame(notes)

InchTommclass = InchTomm()
InchTomm = InchTommclass.GetInchTomm(notes)

Lengthclass = Length()
Length = Lengthclass.GetLength(notes)

notes.add(InchTomm, text='Inches to mm')
notes.add(scaleFrame, text='Scale')
notes.add(Length, text='Scale')
notes.pack(expand=1, fill="both")

ttk.Button(argyle, text="Quit", command=blarg.destroy).grid (column=1, row=1,sticky=E)

blarg.mainloop()
