from typing import List, Any
from pendragonDemesneRandomGeneration import nDX


class Infrastructure:
    def __init__(self):
        # Kind of infrastructure {de-facto, Investment, Enhancement}
        self.kindOf = "Asset"

        # State of operation {Nominal, damaged, destroyed}
        self.status = "Nominal"

        # Properties
        self.buildCost = 0

        self.incomeBase = 0
        self.incomeDie = 6
        self.incomeNumberOfDice = 0

        self.maintenanceBase = 0
        self.maintenanceDie = 6
        self.maintananceNumberOfDice = 0

        self.gloryAnnual = 0
        self.gloryOneTime = 0

        self.rollAnnual = []
        self.checkAnnual = []


    def GenerateIncome(self):
        """
        General purpose generation of an income
        :return: A value in libra
        """
        if (self.incomeDie != 0):
            return self.incomeBase + nDX(self.incomeNumberOfDice, self.incomeDie)
        return self.incomeBase


class Demesne:
    infrastructures: List[Infrastructure]
    deJureTo: Demesne

    def __init__(self):
        # Name of property as used by landowner
        self.name = 'Default Name'

        # Parent property
        self.deJureTo = None

        # List of infrastructure
        self.infrastructures = []

