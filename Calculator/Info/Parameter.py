from tkinter import StringVar

class Parameter:
    
    def __init__(self, beforeText="", afterText=""):
        self.BeforeText = beforeText
        self.EntryTextVar = StringVar()
        self.AfterText = afterText