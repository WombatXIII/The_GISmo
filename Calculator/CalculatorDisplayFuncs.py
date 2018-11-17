from tkinter import ttk,N,W,E,S,Frame

def CreateInput(frame, details, rowPos):
    ttk.Label(frame, text=details.BeforeText).grid(column=2, row=rowPos, sticky=E)
    entry = ttk.Entry(frame, width=7, textvariable= details.EntryTextVar)
    entry.grid(column=3, row=rowPos, sticky=(W, E))
    ttk.Label(frame, text=details.AfterText).grid(column=4, row=rowPos, sticky=W)

def CreateOutputs(frame, details, rowPos):
    ttk.Label(frame, text=details.BeforeText).grid(column=2, row=rowPos, sticky=E)
    ttk.Label(frame, textvariable=details.EntryTextVar).grid(column=3, row=rowPos, sticky=(W, E))
    ttk.Label(frame, text=details.AfterText).grid(column=4, row=rowPos, sticky=W)

def CreateCalculator(parentFrame, details):

    #Creates the title
    ttk.Label(parentFrame, text=details.Title).grid(column=1, row=1, sticky=(W, E))

    rowPos = 3

    #Creates the inputs
    for parameter in details.GetInputs():
        CreateInput(parentFrame, parameter, rowPos)
        rowPos = rowPos + 1
    
    #Creates the outputs
    for parameter in details.GetOutputs():
        CreateOutputs(parentFrame, parameter, rowPos)
        rowPos = rowPos + 1

    #Creates The Button
    ttk.Button(parentFrame, text="Calculate", command=details.Calculate).grid(column=4, row=rowPos, sticky=W)

    #This is hacky way of applying padding. 
    #TODO We should remove this and apply padding to the componenets individually so we don't accidentally override stuff.
    for child in parentFrame.winfo_children(): child.grid_configure(padx=5, pady=5)

def ConfigureCalculatorFrame(calculatorFrame):
    calculatorFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    calculatorFrame.columnconfigure(0, weight=1)
    calculatorFrame.rowconfigure(0, weight=1)

def CreateCalculatorFrame(parentFrame, details):
    calculatorFrame = Frame(parentFrame)
    ConfigureCalculatorFrame(calculatorFrame)
    CreateCalculator(calculatorFrame, details)

    return calculatorFrame