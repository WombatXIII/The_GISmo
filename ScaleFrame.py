from tkinter import *
from tkinter import ttk

class GisScaleFrame: #This is not called scale because scale already exists in tkinter.

    def GetScaleFrame(self, master):

        def trek(*args):
            try:
                rmes = float(ruler.get())
                pmes = float(plan.get())
                dime = float(dim.get())

                red.set((dime / rmes) * pmes)
            except ValueError:
                pass


        frame = Frame(master)
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        ruler = StringVar()
        plan = StringVar()
        dim = StringVar()
        red = StringVar()

        ruler_entry = ttk.Entry(frame, width=7, textvariable=ruler)
        ruler_entry.grid(column=3, row=2, sticky=(W, E))

        plan_entry = ttk.Entry(frame, width=7, textvariable=plan)
        plan_entry.grid(column=3, row=3, sticky=(W, E))

        dim_entry = ttk.Entry(frame, width=7, textvariable=dim)
        dim_entry.grid(column=3, row=4, sticky=(W, E))

        ttk.Label(frame, textvariable=red).grid(column=3, row=5, sticky=(W, E))
        ttk.Button(frame, text="Calculate", command=trek).grid(column=4, row=7, sticky=W)


        ttk.Label(frame, text="Dodgy dimension fixer").grid(column=1, row=1, sticky=W)
        ttk.Label(frame, text="Ruler scale(1:__)").grid(column=2, row=2, sticky=E)
        ttk.Label(frame, text="Plan scale(1:__)").grid(column=2, row=3, sticky=E)
        ttk.Label(frame, text="incorrect dimension (m)").grid(column=2, row=4, sticky=W)
        ttk.Label(frame, text="Converted to dim (m)").grid(column=2, row=5, sticky=E)

        for child in frame.winfo_children(): child.grid_configure(padx=5, pady=5)

        return frame

    def say_hi(self):
        print ("hi there, everyone!")
