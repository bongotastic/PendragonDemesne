import BookOfManorManoralLuck
from Demesne import Infrastructure, Demesne

if __name__ == '__main__':

    myDemesne = Demesne()

    luck = BookOfManorManoralLuck.ManoralLuck()
    luck.Compute(485, myDemesne, None)

