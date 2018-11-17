from tkinter import *
from tkinter import ttk


class InchTomm:

    def GetInchTomm(self, master):

        def calculate(*args):
            try:
                value = float(inches.get())

                mm.set(25.4 * value)
            except ValueError:
                pass

        mainframe = Frame(master)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        inches = StringVar()
        mm = StringVar()

        inches_entry = ttk.Entry(mainframe, width=7, textvariable=inches)
        inches_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(mainframe, textvariable=mm).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="inches").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="mm").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        return mainframe

def say_hi(self):
    print ("Why, hello there!")
