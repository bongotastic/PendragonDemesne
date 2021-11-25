import BookOfManorManoralLuck
from Demesne import Infrastructure, Demesne, DemesneYear

if __name__ == '__main__':

    myDemesne = Demesne()
    myDemesneYear = DemesneYear(myDemesne, 485)


    luck = BookOfManorManoralLuck.ManoralLuck()
    luck.Compute(485, myDemesneYear)

