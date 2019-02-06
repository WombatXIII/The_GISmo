from Calculator.Info.Parameter import Parameter


class ScaleDetails:


    def __init__(self):
        self.Title = "Dodgy dimension fixer"
        self.Ruler = Parameter("Ruler scale(1:__)")
        self.Plan = Parameter("Plan scale(1:__)")
        self.dim = Parameter("incorrect dimension (m)")
        self.ConvertedToDim = Parameter("Converted to dim (m)")

    def GetInputs(self):
        return [self.Ruler, self.Plan, self.dim]

    def GetOutputs(self):
        return [self.ConvertedToDim]

    def Calculate(self, *args):
            try:
                rmes = float(self.Ruler.EntryTextVar.get())
                pmes = float(self.Plan.EntryTextVar.get())
                dime = float(self.dim.EntryTextVar.get())

                self.ConvertedToDim.EntryTextVar.set((dime / rmes) * pmes)
            except ValueError:
                pass
