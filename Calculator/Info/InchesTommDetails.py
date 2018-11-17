from Calculator.Info.Parameter import Parameter

class InchTommDetails:

    def __init__(self):
        self.Title = "Inches"
        self.Inches = Parameter(afterText="inches")
        self.mm = Parameter(beforeText = "is equivalent to", afterText="mm")
    
    def GetInputs(self):
        return [self.Inches]

    def GetOutputs(self):
        return [self.mm]

    def Calculate(self, *args):
            try:
                value = float(self.Inches.EntryTextVar.get())

                self.mm.EntryTextVar.set(25.4 * value)
            except ValueError:
                pass