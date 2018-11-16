from tkinter import *
from tkinter import ttk

class Length: #This is not called scale because scale already exists in tkinter.

    def GetLength(self, master):

        def length(*args):
            try:
                lenlaid = float(laid.get())
                lendigi = float(digi.get())


                perdif.set((lenlaid / lendigi) * 100)
            except ValueError:
                pass


        frame = Frame(master)
        frame.grid(column=0, row=0, sticky=(N, W, E, S))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        laid = StringVar()
        digi = StringVar()
        perdif = StringVar()

        laid_entry = ttk.Entry(frame, width=7, textvariable=laid)
        laid_entry.grid(column=3, row=2, sticky=(W, E))

        digi_entry = ttk.Entry(frame, width=7, textvariable=digi)
        digi_entry.grid(column=3, row=3, sticky=(W, E))


        ttk.Label(frame, textvariable=perdif).grid(column=3, row=5, sticky=(W, E))
        ttk.Button(frame, text="Calculate", command=length).grid(column=4, row=7, sticky=W)


        ttk.Label(frame, text="Precentage Difference").grid(column=1, row=1, sticky=W)
        ttk.Label(frame, text="Laid length").grid(column=2, row=2, sticky=E)
        ttk.Label(frame, text="Digitised length").grid(column=2, row=3, sticky=E)
        ttk.Label(frame, text="%").grid(column=2, row=5, sticky=E)

        for child in frame.winfo_children(): child.grid_configure(padx=5, pady=5)

        return frame

    def say_hi(self):
        print ("hi there, everyone!")
