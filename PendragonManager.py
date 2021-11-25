import BookOfManorManoralLuck
from Demesne import Demesne


class PendragonDemesneStore:
    def __init__(self):
        pass

    def LoadTestSet(self):
        out = []
        for i in range(10):
            out.append(Demesne())
        return out

class PendragonManager:
    def __init__(self):
        self.demesnes = []
        self.currentYear = 485

    def WinterPhase(self):
        # Weather
        manoralLuck = BookOfManorManoralLuck.ManoralLuck()
        manoralLuck.GenerateWeather()

        # Iterate over all demesnes
        for domain in self.demesnes:
            demesneYear = domain.GetYear(self.currentYear)

            # Manoral luck
            manoralLuckOutcome = manoralLuck.Compute(self.currentYear, demesneYear)
            print(manoralLuckOutcome.outcome)


        self.currentYear += 1
