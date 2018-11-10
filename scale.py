from tkinter import *
from tkinter import ttk

def trek(*args):
    try:
        rmes = float(ruler.get())
        pmes = float(plan.get())
        dime = float(dim.get())

        red.set((dime / rmes) * pmes)
    except ValueError:
        pass


root = Tk()
root.title("Dodgy dimension fixer")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ruler = StringVar()
plan = StringVar()
dim = StringVar()
red = StringVar()

ruler_entry = ttk.Entry(mainframe, width=7, textvariable=ruler)
ruler_entry.grid(column=3, row=2, sticky=(W, E))

plan_entry = ttk.Entry(mainframe, width=7, textvariable=plan)
plan_entry.grid(column=3, row=3, sticky=(W, E))

dim_entry = ttk.Entry(mainframe, width=7, textvariable=dim)
dim_entry.grid(column=3, row=4, sticky=(W, E))

ttk.Label(mainframe, textvariable=red).grid(column=3, row=5, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=trek).grid(column=4, row=7, sticky=W)

ttk.Button(mainframe, text="Quit", command=root.destroy) .grid (column=4, row=8,sticky=E)

ttk.Label(mainframe, text="Dodgy dimension fixer").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Ruler scale(1:__)").grid(column=2, row=2, sticky=E)
ttk.Label(mainframe, text="Plan scale(1:__)").grid(column=2, row=3, sticky=E)
ttk.Label(mainframe, text="incorrect dimension (m)").grid(column=2, row=4, sticky=W)
ttk.Label(mainframe, text="Converted to dim (m)").grid(column=2, row=5, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# ruler_entry.focus()
plan_entry.focus()
# dim_entry.focus()
root.bind('return',red)

root.mainloop()
