import BookOfManorManoralLuck
from Demesne import Infrastructure, Demesne, DemesneYear
from PendragonManager import PendragonManager, PendragonDemesneStore

if __name__ == '__main__':
    # Create the engine
    myengine = PendragonManager()
    myengine.demesnes = PendragonDemesneStore().LoadTestSet()
    myengine.WinterPhase()
    myengine

