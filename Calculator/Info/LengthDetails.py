from Calculator.Info.Parameter import Parameter

class LengthDetails:

    def __init__(self):
        self.Title = "Percentage Difference"
        self.Laidlength = Parameter(beforeText="Laid length")
        self.DigitisedLength = Parameter(beforeText = "Digitised length")
        self.PercentageDiff = Parameter(beforeText = "Percentage Difference", afterText = "%")
    
    def GetInputs(self):
        return [self.Laidlength, self.DigitisedLength]

    def GetOutputs(self):
        return [self.PercentageDiff]

    def Calculate(self, *args):
            try:
                Laidlength = float(self.Laidlength.EntryTextVar.get())
                DigitisedLength = float(self.DigitisedLength.EntryTextVar.get())

                self.PercentageDiff.EntryTextVar.set((Laidlength / DigitisedLength) * 100)
            except ValueError:
                pass