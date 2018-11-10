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

tkvar = StringVar(root)

M_1 = {'Scale', 'Laid Length', 'Pack Tracker', 'Referral Tracker'}
tkvar.set('Scale')

popupMenu = OptionMenu(mainframe, tkvar, *M_1)
Label(mainframe, text="Where to?").grid(row=1, column=1)
popupMenu.grid(row=2, column=1)


Label(mainframe, text=" ").grid(row=3, column=1)

def change_dropdown(*args):
    print(tkvar.get())
    import tkvar.get()
    ll()


tkvar.trace('w', change_dropdown)

ttk.Button(mainframe, text="Quit", command=root.destroy).grid(row=6, column=1)

root.mainloop()
