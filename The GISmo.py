import tkinter as tk
from tkinter import Tk, ttk, Frame, N, W, E, S
from Calculator.Info.ScaleDetails import ScaleDetails
from Calculator.Info.LengthDetails import LengthDetails
from Calculator.Info.InchesTommDetails import InchTommDetails
from Calculator.CalculatorDisplayFuncs import CreateCalculatorFrame

TheMainFrame = Tk()
TheMainFrame.title("The GISmo")



# Quit button
argyle = Frame(TheMainFrame)
argyle.grid(column=0, row=0, sticky=(N, W, E, S))
argyle.columnconfigure(0, weight=1)
argyle.rowconfigure(0, weight=1)


ttk.Button(argyle, text="Quit", command=TheMainFrame.destroy).grid (column=1, row=1,sticky=E)
argyle.pack(pady=10, padx=10)

#To add a new calculator to the notebook 
# Step 1 create your own xxDetails Class
# Step 2 pass that into CreateCalculatorFrame function,
# Step 3 then add that frame to the notebook

notes = ttk.Notebook(TheMainFrame)

scaleFrame = CreateCalculatorFrame(notes, ScaleDetails())
notes.add(scaleFrame, text='Scale')

inchTommFrame = CreateCalculatorFrame(notes, InchTommDetails())
notes.add(inchTommFrame, text='Inches to mm')

lengthFrame = CreateCalculatorFrame(notes, LengthDetails())
notes.add(lengthFrame, text='Percentage Difference')


#TODO this interacts oddly with argyle.pack and argyle.grid  We should look up what this done and figure out if there is a better way.
notes.pack(expand=1, fill="both")

#To Keep Tk Inter going until Quit.
TheMainFrame.mainloop()
