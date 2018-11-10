from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Laid Length")


def ll(*args):
    try:
        llen = float(laid.get())
        dlen = float(digi.get())
        tol_p = 5
        tol_m = 2
        tol_md = (tol_m * 2)
        tol_mneg = tol_m - tol_md
        threshold = 40
        if llen >= threshold:
            dif = (llen/dlen)*100
            if dif < (100-tol_p):
                blue.get('Too short')
            if dif >= (100-tol_p) and dif <= (100+tol_p):
                blue.get('Within Tollerance')
            if dif > (100+tol_p):
                blue.get('Too long')
        if llen < threshold:
            dif = llen-dlen
            if dif > tol_m:
                blue.get('Too short')
            if dif < tol_m and dif > tol_mneg:
                blue.get('Within Tollerance')
            if dif < tol_mneg:
                blue.get('Too long')

            except ValueError:
                pass
